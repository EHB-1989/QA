"""
------------------------------------------------------------
 Nom du fichier : locustfile.py
 Auteur        : Moulard Hugo
 Date          : 24/02/2025
 Description   : Task simple pour locust
------------------------------------------------------------
"""

from locust import HttpUser, task, between
import random

class UserAPIUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(1, 2)  # Pause entre les requêtes

    @task
    def get_user(self):
        user_id = random.randint(1, 100)  # Simule différents IDs d'utilisateur
        self.client.get(f"/user/{user_id}")