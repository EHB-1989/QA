from locust import HttpUser, task, between

class TestSortedList(HttpUser):
    wait_time = between(1, 2)
    host = "http://127.0.0.1:5000"

    @task
    def post_sort(self):
        data = self.client.post("/sort", json={"numbers": [4, 3, 2, 1]})
        print(data.json())
