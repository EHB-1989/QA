#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File    :   test_e2e_events_python.py
@Time    :   2025/02/24 14:39:34
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   None
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialisation du navigateur
driver = webdriver.Firefox()

try:
    # Navigation vers la page d'accueil de Python.org
    driver.get("https://www.python.org/")

    # Accéder à la section des événements
    events_link = driver.find_element(By.XPATH, '//li[@id="documentation"]/a')
    events_link.click()

    time.sleep(5)

    events_link = driver.find_element(By.LINK_TEXT, "Beginner’s Guide")
    events_link.click()

    # Vérifier que nous sommes sur la page de l'événement sélectionné
    assert "BeginnersGuide - Python Wiki" in driver.title

    # Attendre quelques secondes pour examiner manuellement la page avant de la fermer
    time.sleep(5)

finally:
    # Fermer le navigateur
    driver.quit()
