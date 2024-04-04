from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(10)
documentation = driver.find_element(By.XPATH, "//a[@href='/doc/']")
documentation.click()

assert "Our Documentation" in driver.title

assert "Browse the docs online or download a copy of your own" in driver.page_source
time.sleep(5)

button = driver.find_element(By.XPATH, "//a[@href='https://wiki.python.org/moin/BeginnersGuide']")
button.click()

assert "BegginnersGuide" in driver.title

assert "Beginner's Guide to Python" in driver.page_source

assert driver.current_url == "https://wiki.python.org/moin/BeginnersGuide"

time.sleep(5)
driver.quit()