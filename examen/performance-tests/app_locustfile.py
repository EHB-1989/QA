from locust import HttpUser, task, between
import random

class APITestUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def get_single_user(self):
        """Requête simple - baseline"""
        user_id = random.randint(1, 10)
        self.client.get(f"/user/{user_id}")

    @task(3)
    def get_same_user_repeatedly(self):
        """
        On appelle plusieurs fois le même user_id 
        version app.py -> repart en BDD à chaque fois (délai de 2s) , tandis que la version optimisée rend le deuxième appel instantané
        """
        self.client.get("/user/1")

    @task(2)
    def get_concurrent_different_users(self):
        """Simule plusieurs utilisateurs différents en parallèle"""
        user_id = random.randint(1, 100)
        self.client.get(f"/user/{user_id}")