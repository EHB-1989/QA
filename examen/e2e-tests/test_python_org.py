import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestPythonOrgE2E(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        brave_paths = [
            r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe")
        ]
        
        brave_executable = None
        for path in brave_paths:
            if os.path.exists(path):
                brave_executable = path
                break
        
        if brave_executable:
            chrome_options.binary_location = brave_executable

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 15)
            self.driver.maximize_window()
        except Exception as e:
            self.fail(f"Impossible de démarrer le navigateur : {e}")

    def test_navigation_to_beginners_guide(self):
        driver = self.driver
        
        # 1. Naviguer à la page d'accueil
        print("Navigation vers python.org...")
        driver.get("https://www.python.org")
        
        # 2. Accéder à la section Documentation
        print("Recherche du lien Documentation...")
        driver.get("https://www.python.org/doc/")

        # 3. Sélectionner une documentation (Beginner's Guide)
        print("Sélection du Beginner's Guide...")
        link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Beginner's Guide")))
        link.click()

        # 4. Vérifier que l'utilisateur est bien sur la page de la documentation sélectionnée
        print("Vérification de la page finale...")
        # On attend simplement que le H1 soit présent
        h1 = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        
        print(f"Titre trouvé : {h1.text}")
        self.assertIn("Beginner", h1.text)
        
        print("Test E2E réussi avec succès !")

    def tearDown(self):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
