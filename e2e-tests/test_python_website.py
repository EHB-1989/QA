from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(2)

events_link = driver.find_element(By.XPATH, '//*[@id="events"]/a')
events_link.click()

time.sleep(2)

python_events_link = driver.find_element(By.XPATH, '//*[@id="events"]/ul/li[1]/a')
python_events_link.click()

driver.get("https://www.python.org/events/")

python_events_link2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div/div/ul/li[2]/h3/a')
python_events_link2.click()

driver.quit()
