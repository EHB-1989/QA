from locust import HttpUser, task

class PerfUser(HttpUser):
    @task
    def perf_est(self):
        self.client.get("/user/1")