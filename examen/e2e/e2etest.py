import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class PythonE2ETest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        # Besoin des sleep sinon j'me fais bloquer par python :(
        url = "https://www.python.org"
        self.driver.get(url)
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Documentation").click()
        sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Beginner's Guide").click()

        self.assertIn("BeginnersGuide", self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
