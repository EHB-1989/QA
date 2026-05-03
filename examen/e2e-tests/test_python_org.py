import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPythonOrgDocumentation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_naviguer_vers_documentation(self):
        driver = self.driver

        # 1. Naviguer à la page d'accueil
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)

        # 2. Accéder à la section Documentation
        doc_link = driver.find_element(By.ID, "documentation")
        doc_link.click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Documentation")
        )
        self.assertIn("Documentation", driver.title)

        # 3. Sélectionner "Beginner's Guide"
        beginners_link = driver.find_element(By.LINK_TEXT, "Beginner's Guide")
        beginners_link.click()

        # 4. Vérifier que l'utilisateur est sur la bonne page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
        heading = driver.find_element(By.ID, "firstHeading")
        self.assertIn("Beginner", heading.text)


if __name__ == '__main__':
    unittest.main()
