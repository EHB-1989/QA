import pytest
from flask_testing import TestCase
from app import app
from gestionnaire_de_taches import GestionnaireDeTaches

class TestIntegration(TestCase):
    # Crée une instance de l'application Flask pour les tests
    def create_app(self):
        # Configure l'application pour les tests
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    # Méthode de configuration exécutée avant chaque test
    def setUp(self):
        # Crée un client de test pour envoyer des requêtes à l'application
        self.app = self.create_app().test_client()
        # Initialise une nouvelle instance du gestionnaire de tâches avec une base de données de test
        self.gestionnaire = GestionnaireDeTaches('test_taches.db')

    # Méthode de nettoyage exécutée après chaque test
    def tearDown(self):
        # Supprime les tables utilisateurs et tâches pour réinitialiser la base de données
        self.gestionnaire.conn.execute('DROP TABLE IF EXISTS utilisateurs')
        self.gestionnaire.conn.execute('DROP TABLE IF EXISTS taches')
        self.gestionnaire.conn.commit()

    # Teste l'ajout d'un utilisateur, l'ajout d'une tâche, et la récupération des tâches
    def test_ajout_et_recuperation_tache(self):
        # Ajout d'un utilisateur via l'API et vérification de la réponse
        response = self.app.post('/utilisateurs', json={
            'nom': 'John Doe',
            'email': 'john@example.com'
        })
        assert response.status_code == 201
        assert response.json == {"message": "Utilisateur créé avec succès"}

        # Ajout d'une tâche pour cet utilisateur via l'API et vérification de la réponse
        response = self.app.post('/taches', json={
            'titre': 'Nouvelle tâche',
            'description': 'Description de la tâche',
            'utilisateur_email': 'john@example.com'
        })
        assert response.status_code == 201
        assert response.json == {"message": "Tâche ajoutée avec succès"}

        # Récupération et vérification des tâches pour l'utilisateur spécifié
        response = self.app.get('/taches/john@example.com')
        taches = response.json
        assert len(taches) == 1
        assert taches[0]['titre'] == 'Nouvelle tâche'
        assert taches[0]['description'] == 'Description de la tâche'

# Exécute les tests si le script est exécuté directement
if __name__ == '__main__':
    pytest.main()
