from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(10)
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("python")
search_box.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in driver.page_source
driver.quit()
