import random
from locust import HttpUser, task, between

class SortingAppUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def sort_numbers(self):
        numbers = [random.randint(1, 100) for _ in range(10)]
        self.client.post("/sort", json={"numbers": numbers})