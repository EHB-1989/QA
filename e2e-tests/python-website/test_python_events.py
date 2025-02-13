import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgEventsE2E(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialisation du navigateur"""
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_python_event_navigation(self):
        """Test de navigation vers un événement Python"""
        driver = self.driver

        # 1. Accéder à la page d'accueil
        driver.get("https://www.python.org")

        # 2. Aller dans la section "Events"
        events_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Events"))
        )
        events_link.click()

        # 3. Attendre que la liste des événements soit visible
        events_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
        )

        # 4. Trouver un événement disponible
        event_links = events_section.find_elements(By.TAG_NAME, "a")

        if not event_links:
            self.fail("Aucun événement trouvé sur la page !")

        # Sélectionner le premier événement de la liste
        first_event = event_links[0]
        event_name = first_event.text
        first_event.click()

        # 5. Vérifier que la page de l'événement est bien ouverte
        WebDriverWait(driver, 10).until(EC.title_contains(event_name))
        self.assertIn(event_name, driver.title, f"L'événement '{event_name}' ne s'est pas ouvert correctement.")

    @classmethod
    def tearDownClass(cls):
        """Fermeture du navigateur"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
