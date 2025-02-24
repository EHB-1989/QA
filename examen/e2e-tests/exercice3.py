import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestPythonOrgDocumentation(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Setup pour initialiser le driver et ouvrir le navigateur"""
        cls.driver = webdriver.Chrome()  
        cls.driver.get("https://www.python.org") 
    
    def test_navigation_to_documentation(self):
        """Vérifier que l'utilisateur peut naviguer vers la documentation"""

        documentation_menu = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Docs")
        documentation_menu.click()

        time.sleep(2)  
        self.assertIn("Documentation", self.driver.title)
        
        beginner_guide_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Beginner's Guide")
        beginner_guide_link.click()
        
        time.sleep(2) 

        self.assertIn("Beginner's Guide", self.driver.title)
        self.assertIn("Python", self.driver.page_source)
    
    @classmethod
    def tearDownClass(cls):
        """Fermer le navigateur après les tests"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
