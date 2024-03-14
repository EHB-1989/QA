from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.google.com")
time.sleep(4)
search_box = driver.find_element("name", "q")
search_box.send_keys("test E2E")
search_box.send_keys(Keys.RETURN)
assert "test E2E" in driver.title
driver.quit()
