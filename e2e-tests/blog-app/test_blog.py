import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time

# Importation de l'application Flask
from app import app  

class BlogE2ETest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Lancement du serveur Flask dans un thread séparé"""
        cls.app = app
        cls.server_thread = Thread(target=cls.app.run, kwargs={'debug': False, 'use_reloader': False})
        cls.server_thread.start()
        time.sleep(5)  # Laisser le serveur démarrer

        # Lancer le navigateur
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)  # Temps d'attente implicite

    def test_create_post(self):
        """Test de création d'un article"""
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        # Aller sur la page de création
        create_link = driver.find_element(By.LINK_TEXT, "Créer un Article")
        create_link.click()
        time.sleep(3)

        # Remplir le formulaire
        title_input = driver.find_element(By.NAME, "title")
        content_input = driver.find_element(By.NAME, "content")

        title_input.send_keys("Titre Test")
        content_input.send_keys("Ceci est un article de test.")

        # Soumettre le formulaire
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        time.sleep(3)  # Attente de la redirection

        # Recharger la page d'accueil
        driver.get("http://127.0.0.1:5000/")
        time.sleep(3)

        # Vérifier que le post est affiché sur la page principale
        self.assertIn("Titre Test", driver.page_source)
        self.assertIn("Ceci est un article de test.", driver.page_source)

    @classmethod
    def tearDownClass(cls):
        """Fermeture du navigateur et arrêt du serveur"""
        cls.driver.quit()
        cls.server_thread.join()

if __name__ == "__main__":
    unittest.main()
