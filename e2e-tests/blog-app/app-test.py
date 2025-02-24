from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

try:
    # Accéder à la page
    driver.get("http://localhost:5000")

    # Attendre que la page soit chargée et vérifier le contenu h1
    titre_blog = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Blog" in titre_blog.text

    # Attendre et cliquer sur le lien "Créer un Article"
    create_article_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Créer un Article"))
    )
    create_article_link.click()

    create_article_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )
    assert create_article_form.is_displayed()

    form_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Titre")),
    )
    form_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Contenu")),
    )

finally:
    # Fermer le navigateur
    driver.quit()