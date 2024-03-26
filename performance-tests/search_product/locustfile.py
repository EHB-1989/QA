from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_api_search(self):
        # self.client.get(f"/item?id={item_id}", name="/item")
        self.client.get(f"/search?query=phone", name="/search")