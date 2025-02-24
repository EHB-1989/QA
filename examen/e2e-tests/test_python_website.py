from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time


def test_access_beginner_guide():
    driver = webdriver.Chrome()

    try:
        # Navigate to the Python.org website
        driver.get("https://www.python.org")

        # Click on the "Documentation" link
        documentation_link = driver.find_element(By.LINK_TEXT, "Documentation")
        documentation_link.click()

        # Wait for the page to load
        time.sleep(2)

        # Click on the "Beginner's Guide" link
        beginners_guide_link = driver.find_element(By.LINK_TEXT, "Beginner's Guide")
        beginners_guide_link.click()

        # Wait for the page to load
        time.sleep(2)

        # Verify that the "Beginner's Guide" page is loaded
        assert "BeginnersGuide" in driver.title
        print("Test Passed: Beginner's Guide page accessed successfully")

    finally:
        # Close the WebDriver
        driver.quit()


# Run the test
test_access_beginner_guide()