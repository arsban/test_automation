import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_driver():
    chrome_options = ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    firefox_options = FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()


def perform_google_search(driver):
    driver.get("https://www.google.com")
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.QS5gu.sy4vM'))
        )
        accept_cookies_button.click()
    except:
        pass

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("google")
    search_box.submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )


def test_google_search_chrome(chrome_driver):
    perform_google_search(chrome_driver)


def test_google_search_firefox(firefox_driver):
    perform_google_search(firefox_driver)
