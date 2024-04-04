from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(2)

events_link = driver.find_element(By.XPATH, '//*[@id="documentation"]/a')
events_link.click()
time.sleep(2)
events_link = driver.find_element(By.XPATH, '//*[@id="container"]/li[3]/ul/li[4]/a')
events_link.click()


driver.get(driver.current_url)

if str(driver.current_url) == "https://devguide.python.org/":
    print("Test passed.")
else:
    print("Test Failed.")