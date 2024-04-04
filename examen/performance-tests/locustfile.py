from locust import HttpUser, task, between
import random

class APITestUser(HttpUser):
    wait_time = between(1, 3)  # Les utilisateurs attendront entre 1 et 3 secondes entre les tâches

    @task
    def get_user_from_db(self):
        self.client.get("/user/" + random.randint(1, 1000000))
