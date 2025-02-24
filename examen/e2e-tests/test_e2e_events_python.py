#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File    :   test_e2e_events_python.py
@Time    :   2025/02/24 14:39:34
@Author  :   FOURMONT Baptiste
@Version :   1.0
@Contact :   baptiste_fourmont@tutanota.com
@Desc    :   Test E2E pour vérifier l'accès au guide du débutant sur Python.org
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PythonOrgTest(unittest.TestCase):

    def setUp(self):
        """Initialisation du navigateur avant chaque test"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(
            10
        )  # Attendre jusqu'à 10 secondes pour les éléments

    def test_navigate_to_beginners_guide(self):
        """Test pour accéder au guide du débutant depuis Python.org"""
        driver = self.driver
        # Naviguer vers la page d'accueil de Python.org
        driver.get("https://www.python.org/")

        # Cliquer sur le lien Documentation
        events_link = driver.find_element(By.XPATH, '//li[@id="documentation"]/a')
        events_link.click()

        # Attendre que la page se charge et cliquer sur le guide du débutant
        guide_link = driver.find_element(By.LINK_TEXT, "Beginner’s Guide")
        guide_link.click()

        # Vérifier que la page du Beginner's Guide est bien chargée
        self.assertIn("BeginnersGuide - Python Wiki", driver.title)

        # Attendre quelques secondes pour l'examen manuel si nécessaire
        time.sleep(5)

    def tearDown(self):
        """Fermer le navigateur après chaque test"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
