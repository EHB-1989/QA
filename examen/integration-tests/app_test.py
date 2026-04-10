import unittest
import json
import os
# Import de l'application Flask et des fonctions de gestion de base
from app import app
from database_manager import init_db, DATABASE_NAME, get_db_connection

class TestIntegrationBibliotheque(unittest.TestCase):

    def setUp(self):
        """Configuration avant chaque test : nettoyage et initialisation de la base SQLite."""
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        # On supprime la base existante pour garantir l'isolation des tests
        if os.path.exists(DATABASE_NAME):
            try:
                os.remove(DATABASE_NAME)
            except PermissionError:
                conn = get_db_connection()
                conn.execute('DELETE FROM livres')
                conn.commit()
                conn.close()
        
        # On recrée la structure et on insère les livres par défaut (1984, etc.)
        init_db()

    def tearDown(self):
        """Nettoyage après le passage de chaque test."""
        if os.path.exists(DATABASE_NAME):
            try:
                os.remove(DATABASE_NAME)
            except PermissionError:
                pass

    # --- TESTS D'AJOUT ---

    def test_ajouter_livre_integration(self):
        """Vérifie l'ajout d'un nouveau livre via l'API et sa persistance réelle en base."""
        nouveau = {'titre': "La Nuit sacrée", 'auteur': 'Tahar Ben Jelloun'}
        response = self.app.post('/ajouter', 
                                 data=json.dumps(nouveau),
                                 content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        
        # Vérification directe dans le fichier SQLite avec fermeture explicite
        conn = get_db_connection()
        livre = conn.execute('SELECT * FROM livres WHERE titre = ?', (nouveau['titre'],)).fetchone()
        self.assertIsNotNone(livre)
        self.assertEqual(livre['auteur'], 'Tahar Ben Jelloun')
        conn.close() # FERMETURE ICI

    # --- TESTS DE LECTURE ---

    def test_lister_livres_integration(self):
        """Vérifie que l'API retourne bien la liste des livres (ceux par défaut + ajouts)."""
        response = self.app.get('/livres')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        # init_db ajoute 3 livres par défaut (Les Misérables, Le Petit Prince, 1984)
        self.assertGreaterEqual(len(data), 3)

    # --- TESTS D'EMPRUNT (Incluant les ajouts logiques) ---

    def test_emprunter_livre_integration(self):
        """Vérifie le succès d'un emprunt pour un livre disponible."""
        # 1. ARRANGE : On s'assure d'insérer un livre tout neuf et disponible juste pour ce test
        titre_test = "L'Enfant de sable"
        conn = get_db_connection()
        conn.execute('INSERT INTO livres (titre, auteur, est_emprunte) VALUES (?, ?, 0)', 
                     (titre_test, 'Tahar Ben Jelloun'))
        conn.commit()
        conn.close()

        # 2. ACT : On tente de l'emprunter via l'API
        payload = {'titre': titre_test}
        response = self.app.post('/emprunter', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        
        # 3. ASSERT : Vérification HTTP
        self.assertEqual(response.status_code, 200)
        
        # Vérification en Base de Données
        conn = get_db_connection()
        livre = conn.execute('SELECT est_emprunte FROM livres WHERE titre = ?', (titre_test,)).fetchone()
        self.assertEqual(livre['est_emprunte'], 1)
        conn.close() # FERMETURE ICI

    def test_emprunter_livre_deja_emprunte(self):
        """[Test Supplémentaire] Vérifie qu'un livre déjà pris ne peut pas être ré-emprunté."""
        payload = {'titre': 'Le Petit Prince'}
        # Premier emprunt
        self.app.post('/emprunter', data=json.dumps(payload), content_type='application/json')
        # Deuxième tentative sur le même titre
        response = self.app.post('/emprunter', data=json.dumps(payload), content_type='application/json')
        
        # L'API doit renvoyer 404 (Livre non disponible)
        self.assertEqual(response.status_code, 404)

    def test_emprunter_livre_inexistant(self):
        """Vérifie l'échec de l'emprunt pour un titre absent de la base."""
        response = self.app.post('/emprunter', 
                                 data=json.dumps({'titre': 'Harry Potter'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 404)

    # --- TESTS DE RETOUR (Incluant les ajouts logiques) ---

    def test_retourner_livre_integration(self):
        """Vérifie qu'un retour via l'API remet le livre à disposition."""
        # 1. On force l'état emprunté en base pour le test
        conn = get_db_connection()
        conn.execute('UPDATE livres SET est_emprunte = 1 WHERE titre = ?', ('1984',))
        conn.commit() # Indispensable pour sauvegarder la modification sans le bloc 'with' !
        conn.close()  # FERMETURE ICI
        
        # 2. Appel de l'API
        response = self.app.post('/retourner', 
                                 data=json.dumps({'titre': '1984'}),
                                 content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        # 3. Vérification de l'état
        conn = get_db_connection()
        livre = conn.execute('SELECT est_emprunte FROM livres WHERE titre = ?', ('1984',)).fetchone()
        self.assertEqual(livre['est_emprunte'], 0)
        conn.close() # FERMETURE ICI

    def test_retourner_livre_deja_disponible(self):
        """[Test Supplémentaire] Vérifie l'échec du retour si le livre n'était pas emprunté."""
        # 'Les Misérables' est disponible (est_emprunte = 0) par défaut
        response = self.app.post('/retourner', 
                                 data=json.dumps({'titre': 'Les Misérables'}),
                                 content_type='application/json')
        
        self.assertEqual(response.status_code, 404)

    # --- TEST DE CYCLE DE VIE ---

    def test_cycle_vie_complet(self):
        """[Test Supplémentaire] Emprunt -> Retour -> Nouvel Emprunt."""
        titre = {'titre': '1984'}
        # 1. Emprunter
        self.app.post('/emprunter', data=json.dumps(titre), content_type='application/json')
        # 2. Retourner
        self.app.post('/retourner', data=json.dumps(titre), content_type='application/json')
        # 3. Ré-emprunter (doit fonctionner)
        response = self.app.post('/emprunter', data=json.dumps(titre), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()