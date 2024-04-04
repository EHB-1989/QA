from locust import HttpUser, task, between
import random

class UserBehavior(HttpUser):
    wait_time = between(1, 2)  # Temps d'attente entre les tâches

    @task
    def get_user(self):
        # Simuler l'accès aux ID d'utilisateurs de manière aléatoire
        user_id = random.randint(1, 10)  
        self.client.get(f"/user/{user_id}", name="/user/[id]")  
