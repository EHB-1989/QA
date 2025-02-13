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
    events_link = driver.find_element(By.XPATH, '//li[@id="downloads"]/a')
    events_link.click()

    # verifier qu'on est sur la pages des evenements
    # assert "Downloads" in driver.title
    title2 = driver.find_element(By.XPATH, "//h2")
    assert "Active Python Releases" in title2.text
    print(title2.text)

    # Attendre que la page des événements se charge
    time.sleep(2)

    # Sélectionner un événement Python spécifique en cliquant sur son lien
    event_link = driver.find_element(By.LINK_TEXT, "Python 3.13.2")
    event_link.click()

    time.sleep(2)

    # Vérifier que nous sommes sur la page de l'événement sélectionné
    assert "Python 3.13.2" in driver.title

    # Attendre quelques secondes pour examiner manuellement la page avant de la fermer
    time.sleep(5)

finally:
    # Fermer le navigateur
    driver.quit()
