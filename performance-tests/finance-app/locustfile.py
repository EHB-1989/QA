from locust import HttpUser, task, between

class APITestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_api_company_financial_report(self):
        self.client.get("/financial_report/1")