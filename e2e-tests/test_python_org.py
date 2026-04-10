import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPythonOrgE2E(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def test_navigation_documentation_beginners_guide(self):
        driver = self.driver

        # Étape 1 Naviguer à la page d'accueil
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)

        # Étape 2 Accéder à la section Documentation
        menu_docs = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Documentation"))
        )
        menu_docs.click()

        # Vérifier qu'on est sur la page Documentation
        self.wait.until(EC.title_contains("Documentation"))
        self.assertIn("/doc", driver.current_url)

        # Étape 3 Sélectionner le Beginner's Guide
        beginners_link = self.wait.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Beginner"))
        )
        beginners_link.click()

        # Étape 4 Vérifier qu'on est bien sur la page Beginner's Guide
        # Le lien peut s'ouvrir dans un nouvel onglet
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])

        self.wait.until(lambda d: "beginner" in d.current_url.lower())
        self.assertIn("beginner", driver.current_url.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
