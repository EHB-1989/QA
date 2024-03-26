from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_api_sort_numbers(self):
        self.client.get("/weather?city=Paris")