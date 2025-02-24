from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class PythonEventsTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_past_events_navigation(self):
        self.browser.get("https://www.python.org/")
        time.sleep(2)  

        # search for the "Events" link
        events_link = self.browser.find_element(By.LINK_TEXT, "Events")
        ActionChains(self.browser).move_to_element(events_link).perform()
        time.sleep(2)

        # click on "Python Events Archive"
        archive_link = self.browser.find_element(By.LINK_TEXT, "Python Events Archive")
        archive_link.click()
        time.sleep(2)

        # try to click on "Python devroom @ FOSDEM 2025"
        specific_event_link = self.browser.find_element(By.LINK_TEXT, "Python devroom @ FOSDEM 2025")
        specific_event_link.click()
        time.sleep(2)

        # check if the title is correct
        self.assertIn("Python devroom @ FOSDEM 2025", self.browser.title)  
        print("Test passed successfully")

if __name__ == '__main__':
    unittest.main()
