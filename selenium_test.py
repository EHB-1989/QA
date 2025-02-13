from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()

driver.get("http://www.python.org")

search_box = driver.find_element("name", "q")

search_box.send_keys("aaaaahejzleza")

search_box.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
sleep(20)
driver.quit()
