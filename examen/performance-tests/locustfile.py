from locust import HttpUser, between, task


class UserApiUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_user(self):
        for user_id in range(1, 6):
            self.client.get(f"/user/{user_id}", name="/user/[id]")
