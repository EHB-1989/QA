from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_user(self):
        user_id = 1  # You can change this to test different user IDs
        self.client.get(f"/user/{user_id}")