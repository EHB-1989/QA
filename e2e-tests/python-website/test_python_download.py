import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configurer le driver de Chrome
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  # Maximiser la fenêtre du navigateur
    yield driver
    driver.quit()

# Scénario de test
def test_download_python_version(driver):
    # Naviguer à la page d'accueil de Python
    driver.get("https://www.python.org")
    
    # Attendre un peu pour que la page se charge
    time.sleep(2)
    
    # Accéder à la section Downloads
    downloads_button = driver.find_element(By.LINK_TEXT, "Downloads")
    downloads_button.click()
    
    # Attendre que la page de téléchargements se charge
    time.sleep(2)
    
    # Vérifier que l'utilisateur est bien sur la page des téléchargements
    assert "Downloads" in driver.title, "L'accès à la page de téléchargements a échoué"
    
    # Vérifier que la dernière version de Python est affichée sur la page
    latest_version_element = driver.find_element(By.XPATH, "//span[contains(@class, 'release-number')]")
    latest_version = latest_version_element.text
    print(f"La dernière version de Python est : {latest_version}")
    
    # Vérifier que la version est un lien de téléchargement valide
    download_button = driver.find_element(By.XPATH, "//a[@href='/download/release/python-" + latest_version.split()[1].replace(".", "") + "/']")
    assert download_button is not None, f"Le téléchargement de la version {latest_version} n'est pas disponible."
    
    # Vérifier que le lien mène bien à une page de téléchargement
    download_button.click()
    time.sleep(2)
    assert "Python Release" in driver.title, f"La page de téléchargement de la version {latest_version} n'a pas été trouvée."

