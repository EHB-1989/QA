from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time


def test_access_beginner_guide():
    driver = webdriver.Chrome()

    try:
        # Va sur le site python
        driver.get("https://www.python.org")

        # Clique su rle menu Documentation
        documentation_link = driver.find_element(By.LINK_TEXT, "Documentation")
        documentation_link.click()

        # Attends le chargement
        time.sleep(2)

        # Clique sur la doc
        beginners_guide_link = driver.find_element(By.LINK_TEXT, "Beginner's Guide")
        beginners_guide_link.click()

        # Attends le chargement
        time.sleep(2)

        # Verification que la page ets bien chargée
        assert "BeginnersGuide" in driver.title
        print("Test Passed: Beginner's Guide page accessed successfully")

    finally:
        # Ferme le WebDriver
        driver.quit()


# Run the test
test_access_beginner_guide()