from locust import HttpUser, task, between
import random

class SortedListPerformanceTest(HttpUser):
    wait_time = between(1, 2) 
    host = "http://localhost:5000"  

    @task
    def send_numbers(self):
        numbers = random.sample(range(1, 1000), 50)  
        self.client.post("/sort", json={"numbers": numbers})
