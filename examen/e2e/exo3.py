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
events_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[1]/ul/li[1]/a')
events_link.click()

driver.get(driver.current_url)

if str(driver.current_url) == "https://wiki.python.org/moin/BeginnersGuide":
    print("vous etes bien sur la page beginners guide")
else :
    print("vous n'etes pas sur la page beginners guide")