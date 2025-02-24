import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgNavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_beginners_guide_navigation(self):
        driver = self.driver
        driver.get("https://www.python.org")

        documentation_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Documentation"))
        )
        documentation_link.click()

        beginners_guide_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Beginner’s Guide"))
        )
        beginners_guide_link.click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Beginner’s Guide")
        )
        
        current_url = driver.current_url
        self.assertIn("beginners-guide", current_url, "La page actuelle n'est pas celle du Beginner’s Guide.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()