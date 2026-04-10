import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPythonDocumentation(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_documentation_beginners_guide(self):
        self.driver.get("https://www.python.org/")

        documentation_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Documentation"))
        )
        documentation_link.click()

        beginners_guide_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Beginner's Guide"))
        )
        beginners_guide_link.click()

        self.wait.until(EC.url_contains("BeginnersGuide"))
        self.assertIn("beginnersguide", self.driver.current_url.lower())
        self.assertTrue(
            "BeginnersGuide" in self.driver.title
        )


if __name__ == "__main__":
    unittest.main()
