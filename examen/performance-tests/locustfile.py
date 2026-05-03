from locust import HttpUser, task, between


class UserBehavior(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_user(self):
        self.client.get("/user/1")

    @task
    def get_multiple_users(self):
        for user_id in range(1, 6):
            self.client.get(f"/user/{user_id}")
