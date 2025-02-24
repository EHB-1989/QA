from locust import HttpUser, task, between
import random

class SortTestUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_sort(self):
        numbers = random.sample(range(10000), 1000)  # Liste aléatoire de 1000 nombres
        self.client.post("/sort", json={"numbers": numbers})

