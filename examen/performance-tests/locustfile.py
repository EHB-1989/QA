from locust import HttpUser, task, between
import random

class DataUser(HttpUser):
    wait_time = between(1, 2)
    @task
    def GetUserData(self):
        self.client.get('/user/' + str(random.randint(0,5)))