from locust import HttpUser, task, between
import json

class SortingServiceUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def sort_numbers(self):
        payload = {
            "numbers": [5, 3, 8, 6, 2, 10, 4, 1, 9, 7]
        }
        headers = {'content-type': 'application/json'}

        self.client.post("/sort", data=json.dumps(payload), headers=headers)