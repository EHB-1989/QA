import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(5)

events_link = driver.find_element(By.XPATH, '//*[@id="documentation"]/a')
events_link.click()
time.sleep(5)
events_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[1]/ul/li[1]/a')
events_link.click()

driver.get(driver.current_url)
assert str(driver.current_url) == "https://docs.python.org/3/"