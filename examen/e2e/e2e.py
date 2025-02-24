import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialisation du navigateur (Chrome ici, sinon changer pour Firefox)
        cls.driver = webdriver.Chrome()  
        cls.driver.maximize_window()  

    def test_acceder_beginner_documentation(self):
        # Accéder à la section Documentation
        self.driver.get("https://www.python.org")
        time.sleep(1)
        doc_link = self.driver.find_element(By.XPATH, '//li[@id="documentation"]/a')
        doc_link.click()
        time.sleep(1) 
        event_link = self.driver.find_element(By.LINK_TEXT, "Beginner’s Guide")
        event_link.click()

        # Vérifier qu'on est bien sur la page de la documentation
        self.assertIn("BeginnersGuide - Python Wiki" , self.driver.title)


if __name__ == "__main__":
    unittest.main()
