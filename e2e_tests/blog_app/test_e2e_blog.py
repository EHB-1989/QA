from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import subprocess
import time
import pytest
import requests


@pytest.fixture(scope="module", autouse=True)
def flask_app():
    """Start the Flask application and ensure it runs before tests."""
    process = subprocess.Popen(
        [sys.executable, "app.py"],
        cwd="e2e_tests/blog_app",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Wait for the server to be available
    for _ in range(10):
        try:
            if requests.get("http://127.0.0.1:5000/").status_code == 200:
                break
        except requests.ConnectionError:
            time.sleep(1)
    else:
        stdout, stderr = process.communicate()
        process.terminate()
        pytest.fail(f"Flask app did not start.\nSTDOUT:\n{stdout.decode()}\nSTDERR:\n{stderr.decode()}")

    yield  # Run tests

    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()

@pytest.fixture
def browser():
    # Setup Chrome WebDriver
    driver = webdriver.Firefox()

    yield driver
    driver.quit()


def test_create_post(browser):
    browser.get('http://127.0.0.1:5000/')

    # Navigate to create post page
    create_link = browser.find_element(By.LINK_TEXT, 'Créer un Article')
    create_link.click()

    # Fill out the form
    title_input = browser.find_element(By.NAME, 'title')
    content_textarea = browser.find_element(By.NAME, 'content')
    title_input.send_keys('Test Title')
    content_textarea.send_keys('Test Content')

    # Submit the form
    submit_button = browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_button.click()

    # Verify the post was created
    assert 'Test Title' in browser.page_source
    assert 'Test Content' in browser.page_source


def test_view_posts(browser):
    browser.get('http://127.0.0.1:5000/')

    # Verify the post is displayed on the index page
    assert 'Test Title' in browser.page_source
    assert 'Test Content' in browser.page_source