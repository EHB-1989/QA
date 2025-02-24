import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PythonOrgDownloadTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_download_latest_version(self):
        driver = self.driver
        driver.get("https://www.python.org/")

        # Navigate to the Downloads page
        download_li = driver.find_element(By.ID, "downloads")
        downloads_link = download_li.find_element(By.TAG_NAME, "a")
        downloads_link.click()

        # Verify that the latest version is available
        latest_version_link = driver.find_element(By.XPATH, "//div[@class='download-os-windows']//a[contains(text(), 'Download Python')]")
        self.assertTrue("Download Python" in latest_version_link.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()