from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_user(self):
        self.client.get("/user/1") 

