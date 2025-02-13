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

        title_input = self.browser.find_element(By.NAME, "title")
        title_input.send_keys("Baptiste article")

        content_input = self.browser.find_element(By.NAME, "content")
        content_input.send_keys("this is a test article for the blog app")

        submit_button = self.browser.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        time.sleep(3)

        content = self.browser.find_element(By.XPATH, "//p")
        self.assertIn("this is a test article for the blog app", content.text)

        title = self.browser.find_element(By.XPATH, "//h2")
        self.assertIn("Baptiste article", title.text)


        print("Test passed")
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
