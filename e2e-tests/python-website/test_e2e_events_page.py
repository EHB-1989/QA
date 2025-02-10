
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialisation du navigateur
driver = webdriver.Firefox()

try:
    # Navigation vers la page d'accueil de Python.org
    driver.get("https://www.python.org/")

    # Accéder à la section des événements
    events_link = driver.find_element(By.XPATH, '//li[@id="events"]/a')
    events_link.click()

    # verifier qu'on est sur la pages des evenements

    
    # Attendre que la page des événements se charge
    time.sleep(2)

    # Sélectionner un événement Python spécifique en cliquant sur son lien
    event_link = driver.find_element(By.LINK_TEXT, "PyConf Hyderabad 2025")
    event_link.click()

    # Vérifier que nous sommes sur la page de l'événement sélectionné
    assert "PyConf Hyderabad 2025" in driver.title

    # Attendre quelques secondes pour examiner manuellement la page avant de la fermer
    time.sleep(5)

finally:
    # Fermer le navigateur
    driver.quit()
