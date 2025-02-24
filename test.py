from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
# ...
sleep(10)