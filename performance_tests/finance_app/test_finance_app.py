import unittest
import time
from app import app as original_app
from optimised_app import app as optimised_app

class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        # Tester l'application originale
        self.client = original_app.test_client()
        self.optimised_client = optimised_app.test_client()
    
    def test_financial_report_response(self):
        response = self.client.get("/financial_report/123")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("company_id", data)
        self.assertIn("report", data)
        print("data1 : ", data)

    def test_optimised_financial_report_response(self):
        response = self.optimised_client.get("/financial_report/123")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("company_id", data)
        self.assertIn("report", data)
        print("data2 : ", data)

    def test_performance_original(self):
        start_time = time.time()
        self.client.get("/financial_report/123")
        elapsed_time = time.time() - start_time
        print(f"Temps de réponse de l'API originale : {elapsed_time:.2f}s")
        self.assertGreaterEqual(elapsed_time, 5, "L'API originale doit prendre au moins 5 secondes.")

    def test_performance_optimised(self):
        start_time = time.time()
        self.optimised_client.get("/financial_report/123")
        elapsed_time = time.time() - start_time
        print(f"Temps de réponse de l'API optimisée : {elapsed_time:.2f}s")
        self.assertLess(elapsed_time, 5, "L'API optimisée devrait être plus rapide que 5 secondes.")

if __name__ == "__main__":
    unittest.main()
