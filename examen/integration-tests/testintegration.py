import unittest
import sqlite3

import database_manager
from app import app

# Connexion en mémoire partagée pour tous les tests (évite les verrous fichier)
_test_conn = sqlite3.connect(":memory:", check_same_thread=False)
_test_conn.row_factory = sqlite3.Row

# Remplacer get_db_connection par une version qui renvoie la connexion en mémoire
database_manager.get_db_connection = lambda: _test_conn


class TestIntegrationBibliotheque(unittest.TestCase):

    def setUp(self):
        """Réinitialise la base de données en mémoire avant chaque test."""
        _test_conn.execute("DROP TABLE IF EXISTS livres")
        _test_conn.commit()
        database_manager.init_db()

        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    # --- Tests de la route GET /livres ---

    def test_lister_livres_initiaux(self):
        """La base de données contient 3 livres par défaut après init_db."""
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        livres = response.get_json()
        self.assertEqual(len(livres), 3)

    def test_lister_livres_retourne_json(self):
        """La route /livres retourne bien du JSON."""
        response = self.client.get('/livres')
        self.assertEqual(response.content_type, 'application/json')

    # --- Tests de la route POST /ajouter ---

    def test_ajouter_livre(self):
        """Ajouter un livre renvoie 201 et le bon message."""
        response = self.client.post(
            '/ajouter',
            json={'titre': 'Dune', 'auteur': 'Frank Herbert'}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['message'], 'Livre ajouté avec succès')

    def test_ajouter_livre_persiste_en_base(self):
        """Un livre ajouté via l'API est bien présent dans la base de données."""
        self.client.post('/ajouter', json={'titre': 'Dune', 'auteur': 'Frank Herbert'})
        response = self.client.get('/livres')
        livres = response.get_json()
        titres = [l['titre'] for l in livres]
        self.assertIn('Dune', titres)

    def test_ajouter_plusieurs_livres(self):
        """Après 2 ajouts, la base contient 5 livres (3 défaut + 2 nouveaux)."""
        self.client.post('/ajouter', json={'titre': 'Dune', 'auteur': 'Frank Herbert'})
        self.client.post('/ajouter', json={'titre': 'Fondation', 'auteur': 'Isaac Asimov'})
        response = self.client.get('/livres')
        livres = response.get_json()
        self.assertEqual(len(livres), 5)

    # --- Tests de la route POST /emprunter ---

    def test_emprunter_livre_disponible(self):
        """Emprunter un livre disponible renvoie 200 et le bon message."""
        response = self.client.post('/emprunter', json={'titre': '1984'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Livre emprunté avec succès')

    def test_emprunter_livre_met_a_jour_base(self):
        """Après emprunt, le livre est marqué est_emprunte=1 en base."""
        self.client.post('/emprunter', json={'titre': '1984'})
        livre = _test_conn.execute("SELECT * FROM livres WHERE titre = '1984'").fetchone()
        self.assertEqual(livre['est_emprunte'], 1)

    def test_emprunter_livre_inexistant(self):
        """Emprunter un livre qui n'existe pas renvoie 404."""
        response = self.client.post('/emprunter', json={'titre': 'Titre Inconnu'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['message'], 'Livre non disponible')

    def test_emprunter_livre_deja_emprunte(self):
        """Emprunter un livre déjà emprunté renvoie 404."""
        self.client.post('/emprunter', json={'titre': '1984'})
        response = self.client.post('/emprunter', json={'titre': '1984'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['message'], 'Livre non disponible')

    # --- Tests de la route POST /retourner ---

    def test_retourner_livre_emprunte(self):
        """Retourner un livre emprunté renvoie 200 et le bon message."""
        self.client.post('/emprunter', json={'titre': 'Le Petit Prince'})
        response = self.client.post('/retourner', json={'titre': 'Le Petit Prince'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Livre retourné avec succès')

    def test_retourner_livre_met_a_jour_base(self):
        """Après retour, le livre est marqué est_emprunte=0 en base."""
        self.client.post('/emprunter', json={'titre': 'Le Petit Prince'})
        self.client.post('/retourner', json={'titre': 'Le Petit Prince'})
        livre = _test_conn.execute("SELECT * FROM livres WHERE titre = 'Le Petit Prince'").fetchone()
        self.assertEqual(livre['est_emprunte'], 0)

    def test_retourner_livre_non_emprunte(self):
        """Retourner un livre qui n'est pas emprunté renvoie 404."""
        response = self.client.post('/retourner', json={'titre': '1984'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['message'], 'Livre non trouvé ou déjà retourné')

    def test_retourner_livre_inexistant(self):
        """Retourner un livre qui n'existe pas renvoie 404."""
        response = self.client.post('/retourner', json={'titre': 'Titre Inconnu'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['message'], 'Livre non trouvé ou déjà retourné')

    def test_retourner_livre_disponible_a_nouveau(self):
        """Un livre retourné peut être emprunté à nouveau."""
        self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        self.client.post('/retourner', json={'titre': 'Les Misérables'})
        response = self.client.post('/emprunter', json={'titre': 'Les Misérables'})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
