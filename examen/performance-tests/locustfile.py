from locust import HttpUser, task, between
import random

class UserBehavior(HttpUser):
    # Temps d'attente entre deux requêtes simulées par un utilisateur (ex: 1s à 2s)
    wait_time = between(1, 2)

    @task
    def get_user(self):
        # On va simuler l'accès à divers utilisateurs par exemple entre l'ID 1 et 10
        user_id = random.randint(1, 10)
        self.client.get(f"/user/{user_id}", name="/user/[id]")
