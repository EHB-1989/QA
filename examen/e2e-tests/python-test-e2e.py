from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")


button_locator = driver.find_element(By.XPATH, '//*[@id="documentation"]/a')
button_locator.click()


time.sleep(2)

download_link = driver.find_element(By.LINK_TEXT, "Beginner's Guide")
download_link.click()

time.sleep(2)

assert "https://wiki.python.org/moin/BeginnersGuide" in driver.current_url


driver.quit()