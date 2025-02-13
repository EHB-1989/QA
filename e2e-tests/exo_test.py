from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialisation du navigateur
driver = webdriver.Chrome()

try:
    # Navigation vers la page d'accueil de Python.org
    driver.get("https://www.python.org/events/python-events/1509/")

    time.sleep(2)

    # Sélectionner l'événement PyCon SK 2024
    pycon_sk_2024_link = driver.find_element(By.LINK_TEXT, "PyCon SK 2024")
    if pycon_sk_2024_link:
        pycon_sk_2024_link.click()

    # Vérifier que nous sommes sur la page de l'événement sélectionné
    assert "PyCon SK 2024" in driver.title
    print("PyCon SK 2024 page is open")

    # Attendre quelques secondes pour examiner manuellement la page avant de la fermer
    time.sleep(5)

finally:
    # Fermer le navigateur
    driver.quit()
