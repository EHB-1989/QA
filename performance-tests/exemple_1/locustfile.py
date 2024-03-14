from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 3)  # Les utilisateurs attendront entre 1 et 3 secondes entre les tâches

    @task
    def get_home(self):
        self.client.get("/")

    @task(2)  # Cette tâche est exécutée avec une probabilité double par rapport à get_home
    def get_api_data(self):
        self.client.get("/api/data")
