from locust import HttpUser, task, between
import random
class PerformanceTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def test(self):
        self.client.get("/user/" + str(random.randint(0, 10)))
