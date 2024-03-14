from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(2)

events_link = driver.find_element(By.XPATH, '//*[@id="downloads"]/a')
events_link.click()

driver.get(driver.current_url)

assert str(driver.current_url) == "https://www.python.org/downloads/"

time.sleep(2)

events_link = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[2]/div/div[2]/p/a')

assert str(events_link.text) == "Download Python 3.12.2"


