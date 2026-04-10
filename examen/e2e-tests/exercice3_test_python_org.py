import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgE2ETest(unittest.TestCase):

    # Initialisation
    def setUp(self):
        self.driver = webdriver.Chrome() # Lancement du navigateur Chrome
        self.driver.maximize_window() # Maximiser la fenêtre pour éviter les problèmes d'affichage
        self.wait = WebDriverWait(self.driver, 10) # WebDriverWait permet d'attendre dynamiquement les éléments

    def test_documentation_flow(self):
        driver = self.driver

        # 1. Aller à la page d'accueil
        driver.get("https://www.python.org")

        # Vérifier que la page est bien chargée
        self.assertIn("Python", driver.title)

        # 2. Accéder à la section Documentation
        doc_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Documentation"))
        )
        doc_link.click()

        # 3. Sélectionner une documentation 
        beginner_guide = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Beginner's Guide"))
        )
        beginner_guide.click()

        # 4. Vérifier que l’utilisateur est sur la bonne page

        # Attente que le titre contienne "Beginner"
        self.wait.until(EC.title_contains("Beginner"))

        # Vérifier le titre de la page
        self.assertIn("Beginner", driver.title)

        # Vérifier l’URL de la page
        self.assertIn("beginners", driver.current_url.lower())

        # Vérifier la présence du titre principal
        h1 = self.wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertTrue(h1)

        # Vérifier que le contenu attendu est présent dans la page
        self.assertIn("Beginner", driver.page_source)

    # Ferme proprement le navigateur
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()