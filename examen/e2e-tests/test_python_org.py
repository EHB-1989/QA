"""
Tests E2E - Exercice 3
Eylon Soussan & Kiara

Scénario testé sur www.python.org :
1. Aller sur la page d'accueil
2. Accéder à la section Documentation
3. Cliquer sur Beginner's Guide
4. Vérifier qu'on est bien sur la bonne page

On utilise Selenium avec unittest.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class TestPythonOrgDocumentation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # configuration du navigateur Chrome en mode headless (sans interface graphique)
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)  # attente implicite de 10s pour trouver les éléments
        cls.wait = WebDriverWait(cls.driver, 15)  # attente explicite pour les conditions

    @classmethod
    def tearDownClass(cls):
        # on ferme le navigateur après tous les tests
        cls.driver.quit()

    def test_01_page_accueil(self):
        # on vérifie que la page d'accueil de python.org se charge bien
        self.driver.get("https://www.python.org")
        self.wait.until(EC.title_contains("Python"))
        self.assertIn("Python", self.driver.title)

    def test_02_acces_documentation(self):
        # on clique sur le lien Documentation dans la barre de navigation
        self.driver.get("https://www.python.org")
        lien_docs = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//nav//a[contains(text(), 'Documentation') or @href='/doc/']")
            )
        )
        lien_docs.click()
        self.wait.until(EC.url_contains("/doc"))
        self.assertIn("/doc", self.driver.current_url)

    def test_03_cliquer_beginners_guide(self):
        # depuis la page documentation, on clique sur Beginner's Guide
        self.driver.get("https://www.python.org/doc/")

        # on utilise PARTIAL_LINK_TEXT car le lien contient une apostrophe typographique
        lien_beginner = self.wait.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Beginner"))
        )
        lien_beginner.click()

        # on vérifie que la page chargée correspond bien au Beginner's Guide
        self.wait.until(EC.url_contains("BeginnersGuide"))

    def test_04_verification_page_beginners_guide(self):
        # scénario complet : accueil -> documentation -> Beginner's Guide -> vérification

        # étape 1 : page d'accueil
        self.driver.get("https://www.python.org")
        self.wait.until(EC.title_contains("Python"))

        # étape 2 : page documentation
        self.driver.get("https://www.python.org/doc/")
        self.wait.until(EC.url_contains("/doc"))

        # étape 3 : cliquer sur Beginner's Guide
        lien_beginner = self.wait.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Beginner"))
        )
        lien_beginner.click()

        # étape 4 : vérifier qu'on est bien sur la page du Beginner's Guide
        self.wait.until(EC.url_contains("BeginnersGuide"))
        self.assertIn(
            "BeginnersGuide",
            self.driver.current_url,
            msg=f"Mauvaise page - URL: {self.driver.current_url}"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
