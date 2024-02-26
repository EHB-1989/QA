import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  

    def tearDown(self):
        self.browser.quit()

    def test_create_post(self):
        self.browser.get('http://localhost:5000/')
        self.browser.find_element(By.LINK_TEXT, 'Créer un Article').click()
        self.browser.find_element(By.NAME, 'title').send_keys('Mon Premier Article')
        self.browser.find_element(By.NAME, 'content').send_keys('Ceci est le contenu de mon premier article.')
        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        sleep(1)  # Laisser le temps à la page de se rafraîchir
        body = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertIn('Mon Premier Article', body)

if __name__ == '__main__':
    unittest.main()
