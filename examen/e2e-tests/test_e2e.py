import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPythonOrgE2E(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_navigation_documentation_beginners_guide(self):
        self.driver.get("https://www.python.org")
        self.assertIn("Python", self.driver.title)

        self.driver.get("https://docs.python.org/3/")
        self.assertIn("docs.python.org", self.driver.current_url)

        self.driver.get("https://wiki.python.org/moin/BeginnersGuide")

        self.assertIn("BeginnersGuide", self.driver.current_url)

        heading = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertIn("Beginner", heading.text)


if __name__ == '__main__':
    unittest.main()