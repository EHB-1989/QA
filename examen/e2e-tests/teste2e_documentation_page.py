import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDocumentationPage(unittest.TestCase):

    def setUp(self):
        """Initialise le navigateur avant chaque test."""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Ferme le navigateur après chaque test."""
        self.driver.quit()

    def test_acceder_beginners_guide(self):
        driver = self.driver

        # 1. Naviguer à la page d'accueil
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)

        # 2. Accéder à la section Documentation
        documentation_link = driver.find_element(By.XPATH, '//li[@id="documentation"]/a')
        documentation_link.click()
        time.sleep(2)

        # Vérifier qu'on est bien sur la page de documentation
        self.assertIn("Documentation", driver.title)

        # 3. Sélectionner la documentation "Beginner's Guide"
        beginners_guide_link = driver.find_element(By.LINK_TEXT, "Beginner's Guide")
        beginners_guide_link.click()
        time.sleep(3)

        # 4. Vérifier que l'utilisateur est sur la page de la documentation sélectionnée
        self.assertIn("BeginnersGuide", driver.title)


if __name__ == "__main__":
    unittest.main()
