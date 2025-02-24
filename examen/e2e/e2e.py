import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try : 
        # Initialisation du navigateur Chrome car le Driver Firefox ne passe pas sur mon Linux
        driver = webdriver.Chrome()  

        #Naviguer à la page d'accueil
        driver.get("https://www.python.org")
        time.sleep(1) 

        # Accéder à la section Documentation
        doc_link = driver.find_element(By.XPATH, '//li[@id="documentation"]/a')
        doc_link.click()
        time.sleep(1)  # Attendre le chargement

        event_link = driver.find_element(By.LINK_TEXT, "Beginner’s Guide")
        event_link.click()

        # Vérifier qu'on est bien sur la page de la documentation beginner
        assert "BeginnersGuide - Python Wiki" in driver.title
        
finally:

    driver.quit()