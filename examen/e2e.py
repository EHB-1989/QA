import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()

  def test_parcours_utilisateur(self):
    self.driver.get("https://www.python.org")

    docs_link = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "documentation"))
    )
    docs_link.click()

    beginners_guide_link = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Beginner's Guide"))
    )
    beginners_guide_link.click()

    self.assertIn("Beginner", self.driver.title)

  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
  unittest.main()