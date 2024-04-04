import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navigation_documentation(self):
        driver = self.driver
        driver.get("http://www.python.org")  
        assert "Python" in driver.title  
        
        # acceder à la documention
        documentation_link = driver.find_element(By.LINK_TEXT, "Documentation")
        documentation_link.click()
        
        # selectionner
        beginners_guide_link = driver.find_element(By.LINK_TEXT, "Beginner’s Guide")
        beginners_guide_link.click()
        
        # verifier que l'utilisateur est bien sur la page 
        assert "Beginner’s Guide" in driver.page_source
        #en vérifiant l'URL actuelle aussi
        assert "BeginnersGuide", driver.current_url

    def tearDown(self):
        self.driver.close() 

if __name__ == "__main__":
    unittest.main()
