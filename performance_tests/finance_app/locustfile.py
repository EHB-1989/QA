from locust import HttpUser, task, between

class FinancialReportUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_financial_report(self):
        self.client.get("/financial_report/123")
