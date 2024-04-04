from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# time.sleep(10)
# search_box = driver.find_element(By.XPATH, '//input[@id="id-search-field"]')
# search_box.send_keys("python")
# search_box.send_keys(Keys.RETURN)
# time.sleep(5)
# assert "No results found." not in driver.page_source
# driver.quit()


# scenario check python event

driver = webdriver.Firefox()
driver.get("http://www.python.org")

# cliquer sur le button event 
button_locator = driver.find_element(By.XPATH, '//*[@id="documentation"]/a')
button_locator.click()

time.sleep(2)

button_locator = driver.find_element(By.LINK_TEXT, "Beginner's Guide")
button_locator.click()

assert "https://wiki.python.org/moin/BeginnersGuide" in driver.current_url

driver.quit()




