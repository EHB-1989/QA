from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# init
driver = webdriver.Firefox()

# navigate
driver.get("http://www.python.org")
time.sleep(1)

# cliquer sur le bouton documentation
events_link = driver.find_element(By.XPATH, '//*[@id="documentation"]/a')
events_link.click()
time.sleep(1)

# cliquer sur le premier lien proposé, actuellement : Beginners Guide
events_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[1]/ul/li[1]/a')
events_link.click()

# recuperation de l'url actuel
driver.get(driver.current_url)

# test de coherence, retourne une erreur en cas de non concordence
assert (str(driver.current_url) == "https://wiki.python.org/moin/BeginnersGuide")

driver.quit()