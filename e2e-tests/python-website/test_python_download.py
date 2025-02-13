import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonDownloadTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialisation du navigateur"""
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_download_latest_python(self):
        """Test de téléchargement de la dernière version de Python"""
        driver = self.driver

        # 1. Accéder à la page d'accueil
        driver.get("https://www.python.org")

        # 2. Aller dans la section "Downloads"
        downloads_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Downloads"))
        )
        downloads_link.click()

        # 3. Vérifier qu'on est bien sur la page des téléchargements
        self.assertIn("Download Python", driver.title, "La page de téléchargement ne s'est pas ouverte.")

        # 4. Trouver la dernière version de Python
        latest_version_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='release-number']/a"))
        )
        latest_version_text = latest_version_element.text
        print(f"Dernière version détectée : {latest_version_text}")

        # 5. Vérifier que le bouton de téléchargement est bien présent
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Download Python')]"))
        )
        download_link = download_button.get_attribute("href")

        self.assertTrue(download_link.startswith("https://www.python.org/ftp/python/"),
                        "Le lien de téléchargement ne semble pas valide.")

        print(f"Lien de téléchargement trouvé : {download_link}")

    @classmethod
    def tearDownClass(cls):
        """Fermeture du navigateur"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
