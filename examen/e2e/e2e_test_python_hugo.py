"""
------------------------------------------------------------
 Nom du fichier : e2e_test_python_hugo.py
 Auteur        : Moulard Hugo
 Date          : 24/02/2025
 Description   : Test end 2 end sur python.org
------------------------------------------------------------
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PythonOrgTest(unittest.TestCase):

    def setUp(self):
        """Initialisation du WebDriver"""
        self.driver = webdriver.Chrome()

    def test_navigation_to_beginners_guide(self):
        """Test de navigation vers le Beginner’s Guide"""

        driver = self.driver
        driver.get("https://www.python.org")  # 1. Ouvrir la page d'accueil

        # 2. Accéder à la section "Documentation"
        doc_link = driver.find_element(By.LINK_TEXT, "Documentation")
        doc_link.click()

        # 3. Cliquer sur "Beginner’s Guide"
        beginner_guide_link = driver.find_element(By.LINK_TEXT, "Beginner’s Guide")
        beginner_guide_link.click()

        # 4. Vérifier que l'on est bien sur la page "Beginner’s Guide"
        expected_url = "https://wiki.python.org/moin/BeginnersGuide"
        self.assertEqual(driver.current_url, expected_url, "L'URL ne correspond pas au Beginner’s Guide")

    def tearDown(self):
        """Fermeture du navigateur"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
