from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 3)  # Les utilisateurs attendront entre 1 et 3 secondes entre les tâches

    @task
    def get_user(self):
        self.client.get("/user/1234")
