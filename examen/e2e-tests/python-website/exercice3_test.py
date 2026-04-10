import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgE2ETests(unittest.TestCase):

    def setUp(self):
        # Initialiser le driver (ici on utilise Edge ou Chrome selon ce qui est dispo)
        # Chrome est un standard, s'assure qu'il fonctionne headless ou normal
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Optionnel : décocher pour voir le navigateur
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def test_navigation_documentation_beginner_guide(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # 1. Naviguer à la page d'accueil
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)

        # 2. Accéder à la section Documentation
        # Le bouton de "Documentation" en haut dans le menu de navigation
        documentation_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Documentation"))
        )
        documentation_link.click()

        # Vérifier qu'on est bien sur la page doc
        wait.until(EC.title_contains("Documentation"))

        # 3. Sélectionner une documentation (exemple: Beginner's Guide)
        # Sur la page /doc/, on recherche le lien vers le Beginner's Guide
        beginner_guide_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Beginner's Guide"))
        )
        beginner_guide_link.click()

        # 4. Vérifier que l'utilisateur est bien sur la page selectionnée.
        # Le guide du débutant amène souvent sur le wiki "BeginnersGuide"
        wait.until(EC.url_contains("BeginnersGuide"))
        
        # On vérifie aussi que le titre ou le contenu a chargé
        self.assertTrue(
            "Beginner" in driver.title or "BeginnersGuide" in driver.current_url,
            "La page de destination ne semble pas être le Beginner's Guide"
        )

    def tearDown(self):
        # Fermer le navigateur après le test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
