from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def create_item(self):
        data = {
            "name": "Test Item",
            "description": "This is a test item"
        }
        self.client.post("/api/items", json=data)

    @task
    def simulate_long_processing(self):
        self.client.get("/api/simulate_long_processing")

    @task
    def get_data(self):
        self.client.get("/api/data")
