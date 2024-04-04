from locust import HttpUser, task, between

class UserAccessUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_user(self):
        user_id = 1 
        self.client.get(f"/user/{user_id}", name="/user")
