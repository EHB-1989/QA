
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
  driver.get('https://www.python.org/')
  events_link = driver.find_element(By.LINK_TEXT, 'Documentation')
  events_link.click()

  assert "Documentation" in driver.title

  # Wait for the page to load.
  time.sleep(2)

  event_link = driver.find_element(By.LINK_TEXT, "Beginner’s Guide")
  event_link.click()

  documentation_title = driver.find_element(By.CSS_SELECTOR, 'h1#Beginner\\.27s_Guide_to_Python')
  assert "Beginner's Guide to Python" in documentation_title.text

finally:
  driver.quit()
