import unittest
import sqlite3
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

import database_manager
from app import app


# Crée la table livres dans la base de test
def init_test_db(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS livres
                 (id INTEGER PRIMARY KEY, titre TEXT, auteur TEXT, est_emprunte BOOLEAN)''')
    conn.commit()


# Retourne une connexion vers une base SQLite en mémoire (isolée, sans fichier)
def get_test_db_connection():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    init_test_db(conn)
    return conn


# Tests d'intégration : on teste les routes Flask avec une vraie base de données
class TestIntegration(unittest.TestCase):

    def setUp(self):
        # On remplace la vraie BDD par une BDD en mémoire avant chaque test
        self.test_conn = get_test_db_connection()
        self.conn_patcher = patch(
            'database_manager.get_db_connection',
            return_value=self.test_conn
        )
        self.conn_patcher.start()

        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        # On nettoie la BDD et le mock après chaque test
        self.conn_patcher.stop()
        self.test_conn.close()

    #  Tests /ajouter 

    def test_ajouter_livre(self):
        # Ajouter un livre doit retourner 201 avec un message de succès
        response = self.client.post('/ajouter', json={
            'titre': 'Clean Code',
            'auteur': 'Robert Martin'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['message'], 'Livre ajouté avec succès')

    def test_ajouter_plusieurs_livres(self):
        # Ajouter 2 livres doit bien les stocker tous les deux
        self.client.post('/ajouter', json={'titre': 'Livre A', 'auteur': 'Auteur A'})
        self.client.post('/ajouter', json={'titre': 'Livre B', 'auteur': 'Auteur B'})
        response = self.client.get('/livres')
        livres = response.get_json()
        self.assertEqual(len(livres), 2)

    #  Tests /livres 

    def test_lister_livres_vide(self):
        # Sans aucun livre ajouté, la liste doit être vide
        response = self.client.get('/livres')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_lister_livres_apres_ajout(self):
        # Après ajout, le livre doit apparaître dans la liste avec les bons attributs
        self.client.post('/ajouter', json={'titre': '1984', 'auteur': 'George Orwell'})
        response = self.client.get('/livres')
        livres = response.get_json()
        self.assertEqual(len(livres), 1)
        self.assertEqual(livres[0]['titre'], '1984')
        self.assertEqual(livres[0]['auteur'], 'George Orwell')
        self.assertFalse(livres[0]['est_emprunte'])

    #  Tests /emprunter 

    def test_emprunter_livre_disponible(self):
        # Emprunter un livre disponible doit retourner 200
        self.client.post('/ajouter', json={'titre': 'Python 3', 'auteur': 'Lutz'})
        response = self.client.post('/emprunter', json={'titre': 'Python 3'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Livre emprunté avec succès')

    def test_emprunter_livre_inexistant(self):
        # Emprunter un livre qui n'existe pas doit retourner 404
        response = self.client.post('/emprunter', json={'titre': 'Livre Inexistant'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['message'], 'Livre non disponible')

    def test_emprunter_livre_deja_emprunte(self):
        # Emprunter deux fois le même livre doit échouer la 2ème fois
        self.client.post('/ajouter', json={'titre': 'Flask Web', 'auteur': 'Grinberg'})
        self.client.post('/emprunter', json={'titre': 'Flask Web'})
        response = self.client.post('/emprunter', json={'titre': 'Flask Web'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['message'], 'Livre non disponible')

    def test_emprunter_marque_livre_comme_emprunte(self):
        # Après emprunt, le livre doit être marqué comme emprunté en base
        self.client.post('/ajouter', json={'titre': 'Design Patterns', 'auteur': 'GoF'})
        self.client.post('/emprunter', json={'titre': 'Design Patterns'})
        livres = self.client.get('/livres').get_json()
        self.assertTrue(livres[0]['est_emprunte'])

    #  Tests /retourner 

    def test_retourner_livre_emprunte(self):
        # Retourner un livre emprunté doit retourner 200
        self.client.post('/ajouter', json={'titre': 'Le Seigneur', 'auteur': 'Tolkien'})
        self.client.post('/emprunter', json={'titre': 'Le Seigneur'})
        response = self.client.post('/retourner', json={'titre': 'Le Seigneur'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Livre retourné avec succès')

    def test_retourner_livre_non_emprunte(self):
        # Retourner un livre qui n'est pas emprunté doit retourner 404
        self.client.post('/ajouter', json={'titre': 'Dune', 'auteur': 'Herbert'})
        response = self.client.post('/retourner', json={'titre': 'Dune'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()['message'], 'Livre non trouvé ou déjà retourné')

    def test_retourner_livre_inexistant(self):
        # Retourner un livre qui n'existe pas doit retourner 404
        response = self.client.post('/retourner', json={'titre': 'Inconnu'})
        self.assertEqual(response.status_code, 404)

    def test_retourner_remet_livre_disponible(self):
        # Après retour, le livre doit être à nouveau disponible en base
        self.client.post('/ajouter', json={'titre': 'Sapiens', 'auteur': 'Harari'})
        self.client.post('/emprunter', json={'titre': 'Sapiens'})
        self.client.post('/retourner', json={'titre': 'Sapiens'})
        livres = self.client.get('/livres').get_json()
        self.assertFalse(livres[0]['est_emprunte'])

    #  Test cycle complet 

    def test_cycle_complet(self):
        # On simule un cycle entier : ajout → emprunt → vérification → retour → vérification
        r = self.client.post('/ajouter', json={'titre': 'Clean Architecture', 'auteur': 'Martin'})
        self.assertEqual(r.status_code, 201)

        r = self.client.post('/emprunter', json={'titre': 'Clean Architecture'})
        self.assertEqual(r.status_code, 200)

        # Le livre doit être marqué emprunté
        livres = self.client.get('/livres').get_json()
        self.assertTrue(livres[0]['est_emprunte'])

        r = self.client.post('/retourner', json={'titre': 'Clean Architecture'})
        self.assertEqual(r.status_code, 200)

        # Le livre doit être à nouveau disponible
        livres = self.client.get('/livres').get_json()
        self.assertFalse(livres[0]['est_emprunte'])


if __name__ == '__main__':
    unittest.main()
