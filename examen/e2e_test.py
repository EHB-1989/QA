import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPythonOrgE2E(unittest.TestCase):

    def setUp(self):
        """Préparation : j'ouvre le navigateur avant le test."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_navigation_beginners_guide(self):
        """Scénario E2E : Accueil -> Documentation -> Beginner's Guide."""
        driver = self.driver
        # Je définis une attente explicite de 10 secondes maximum.
        # Pour éviter que le test crash si la connexion est lente.
        wait = WebDriverWait(driver, 10)

        # 1. Naviguer à la page d'accueil
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title) # Je vérifie que je suis bien sur le bon site

        # 2. Accéder à la section Documentation
        # J'attends que le bouton soit cliquable avant de cliquer dessus
        lien_doc = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Documentation")))
        lien_doc.click()

        # 3. Sélectionner la documentation (Beginner's Guide)
        lien_beginner = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Beginner's Guide")))
        lien_beginner.click()

        # 4. Vérifier que l'utilisateur est bien sur la page sélectionnée
        # La page du Beginner's Guide contient "BeginnersGuide" dans son URL
        # J'attends que l'URL change pour faire ma vérification finale
        wait.until(EC.url_contains("BeginnersGuide"))
        
        # Assertion finale : je valide que l'URL actuelle est la bonne
        self.assertIn("BeginnersGuide", driver.current_url)

    def tearDown(self):
        """Nettoyage : je ferme le navigateur après le test."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()