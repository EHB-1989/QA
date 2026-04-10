"""
Tests de performance - Exercice 4 (optionnel)
Eylon Soussan & Kiara

L'application app.py simule une base de données lente avec un délai de 2 secondes.
On utilise Locust pour mesurer les performances.

Pour lancer :
    locust -f locustfile.py --host=http://localhost:5000
Puis ouvrir http://localhost:8089

Ou sans interface :
    locust -f locustfile.py --host=http://localhost:5000 --headless -u 10 -r 2 -t 30s
"""

from locust import HttpUser, task, between
import random


class UtilisateurTest(HttpUser):
    # on simule un délai entre les requêtes pour reproduire un comportement réel
    wait_time = between(1, 3)

    @task(1)
    def get_utilisateur(self):
        # on récupère l'utilisateur avec l'ID 1
        # on s'attend à un temps de réponse > 2s à cause du délai simulé
        with self.client.get("/user/1", catch_response=True) as reponse:
            if reponse.status_code == 200:
                reponse.success()
            else:
                reponse.failure(f"Code inattendu : {reponse.status_code}")

    @task(1)
    def get_utilisateur_aleatoire(self):
        # on varie les IDs pour simuler plusieurs utilisateurs différents
        user_id = random.randint(1, 100)
        with self.client.get(f"/user/{user_id}", catch_response=True) as reponse:
            if reponse.status_code == 200:
                reponse.success()
            else:
                reponse.failure(f"Erreur pour ID {user_id} : {reponse.status_code}")
