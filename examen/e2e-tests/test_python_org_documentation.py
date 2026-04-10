"""
Parcours e2e (Selenium + unittest) sur www.python.org :
accueil → Documentation → Beginner's Guide → vérification de la page cible.
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestPythonOrgDocumentation(unittest.TestCase):
    """Scénario utilisateur : navigation vers une page de documentation."""

    @classmethod
    def setUpClass(cls):
        cls.base_url = "https://www.python.org/"
        cls.doc_path = "/doc/"
        cls.beginners_wiki_path = "BeginnersGuide"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def test_navigation_vers_beginners_guide(self):
        """Accueil → section Documentation → Beginner's Guide → page wiki attendue."""
        driver = self.driver
        wait = self.wait

        driver.get(self.base_url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Accès à la section Documentation (lien principal du menu)
        doc_entry = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "li#documentation > a[href='/doc/']")
            )
        )
        doc_entry.click()
        wait.until(EC.url_contains(self.doc_path))

        # Sélection d'une documentation : Beginner's Guide (lien du corps de page,
        # pas le sous-menu latéral qui peut rester non interactif tant qu'il n'est pas ouvert)
        beginner_link = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "div.beginner-widget a[href*='BeginnersGuide']",
                )
            )
        )
        beginner_link.click()
        wait.until(EC.title_contains("BeginnersGuide"))
        self.assertIn("wiki.python.org", driver.current_url)
        self.assertIn(self.beginners_wiki_path, driver.current_url)
        self.assertIn("BeginnersGuide", driver.title)


if __name__ == "__main__":
    unittest.main(verbosity=2)
