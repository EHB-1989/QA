from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_home(self):
        self.client.get("/")

    @task(2)
    def get_api_simulate_long_processing(self):
        self.client.get("/api/simulate_long_processing")

    @task(3)
    def post_api_create_item(self):
        self.client.post("/api/items", json={"name":"Une référence", "description":"une description"})