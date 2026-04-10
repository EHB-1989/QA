import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestPythonOrg(unittest.TestCase):

    def setUp(self):
        service = Service("/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(service=service)

    def test_parcours_utilisateur(self):
        driver = self.driver

        # 1. Accueil
        driver.get("https://www.python.org")

        # 2. Documentation
        driver.find_element(By.LINK_TEXT, "Documentation").click()

        # 3. Beginner’s Guide
        driver.find_element(By.LINK_TEXT, "Beginner’s Guide").click()

        # 4. Vérification
        self.assertIn("Beginner", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
