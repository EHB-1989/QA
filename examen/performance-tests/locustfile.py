from locust import HttpUser, task, between
import random

class UserBehavior(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_user(self):
        user_id = random.randint(1, 10)
        self.client.get(f"/user/{user_id}")
