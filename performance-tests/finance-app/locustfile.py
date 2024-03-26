from locust import HttpUser, task, between

class FinancialReportUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_financial_report(self):
        company_id = "AIRBUS" 
        self.client.get(f"/financial_report/{company_id}", name="/financial_report")
