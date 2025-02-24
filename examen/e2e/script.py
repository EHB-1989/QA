from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class PythonDocumentationTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_navigation_to_beginners_guide(self):
        self.browser.get("https://www.python.org/")
        time.sleep(2)  

        # I wait for the "Documentation" menu to be present
        doc_menu = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "documentation"))
        )

        # Mooving the mouse to the "Documentation" menu
        ActionChains(self.browser).move_to_element(doc_menu).perform()
        time.sleep(2)  

        # I wait a bit for the "Beginner's Guide" link to be clickable
        beginners_guide_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), \"Beginner\")]"))
        )
        beginners_guide_link.click()
        time.sleep(2)  

        # Finally, I check if the url and title contain "BeginnersGuide"
        self.assertIn("BeginnersGuide", self.browser.current_url)
        self.assertIn("BeginnersGuide", self.browser.title)
        print("Test passed successfully we are on the Beginners Guide page !")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
