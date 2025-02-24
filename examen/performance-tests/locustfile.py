import random

from locust import HttpUser, task, between

class AppUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_user(self):
        user_id = random.randint(1, 100)
        self.client.get(f"/user/{user_id}")