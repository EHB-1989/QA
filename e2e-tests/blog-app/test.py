from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://127.0.0.1:5000")
# ...
sleep(10)