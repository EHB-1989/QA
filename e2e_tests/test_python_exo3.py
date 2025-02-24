from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class PythonDownloadTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_download_latest_python(self):
        """ Test that we can access the download page for the latest version of Python (dynamic test) """
        self.browser.get("https://www.python.org/")
        time.sleep(2)  

        # find the "Downloads" link
        downloads_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Downloads")
        downloads_link.click()

        
        WebDriverWait(self.browser, 10).until(
            EC.title_contains("Download Python | Python.org")
        )
        self.assertIn("Download Python | Python.org", self.browser.title)  # check if the title is correct
        print("Access to the download page verified.")

        # Here we retrieve all the available versions
        versions_elements = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list-row-container.menu .release-number a"))
        )

        # then extract the text and links
        versions = [element.text for element in versions_elements]
        release_links = [element.get_attribute("href") for element in versions_elements]
        print(f"Available versions: {versions}")

        # Try to access the release page for each version
        for version, link in zip(versions, release_links):
            try:
                print(f"Trying to access the release page for version {version}...")
                self.browser.get(link)

                # wait for the page to load
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1.page-title"))
                )
                
                # check if the title is correct
                page_title = self.browser.find_element(By.CSS_SELECTOR, "h1.page-title").text
                self.assertEqual(page_title, f"{version}")
                print(f"Page for version {version} is correct.")
                
                # if the page is correct, we can stop the loop
                break
            except Exception as e:
                print(f"error for version {version}: {e}")
                continue  # try the next version

        else:
            self.fail("No version page was correct")

if __name__ == '__main__':
    unittest.main()
