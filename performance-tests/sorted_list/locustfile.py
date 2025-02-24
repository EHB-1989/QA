from locust import HttpUser, task

class SortUser(HttpUser):
    @task
    def sort(self):
        self.client.post("/sort", json={"numbers": [5, 3, 8, 1, 2]})