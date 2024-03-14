from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# scenario check python event

driver = webdriver.Edge()
driver.get("http://www.python.org")

# cliquer sur le button download 
button_locator = driver.find_element(By.XPATH, '//*[@id="downloads"]/a')
button_locator.click()

# Verifier qu'on est bien sur la page des events 

# cliquer sur le button download 
driver.get(driver.current_url)
events_link = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[2]/div/div[2]/p/a')
x = str(events_link.text)
assert str("Download Python 3.12.2") in x
print('ok')

driver.quit()




