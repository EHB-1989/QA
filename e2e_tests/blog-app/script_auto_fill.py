from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class BlogAppTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_blog_app(self):
        self.browser.get("http://localhost:5000/create")

        # fill the title input
        title_input = self.browser.find_element(By.NAME, "title")
        title_input.send_keys("Wassim article")

        # fill the content input
        content_input = self.browser.find_element(By.NAME, "content")
        content_input.send_keys("this is a test article for the blog app")

        # submit the form
        submit_button = self.browser.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        time.sleep(3)

        title = self.browser.find_element(By.XPATH, "//h2")
        self.assertIn("Wassim article", title.text)

        content = self.browser.find_element(By.XPATH, "//p")
        self.assertIn("this is a test article for the blog app", content.text)
       
        print("Test passed")
        time.sleep(3)

    

if __name__ == '__main__':
    unittest.main()
