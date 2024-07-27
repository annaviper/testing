import pytest
import time
from selenium import webdriver
from RandomProject.pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    time.sleep(1)

    login_page.enter_username("test")
    time.sleep(1)

    login_page.enter_password("test")
    time.sleep(1)
    
    login_page.click_login()
    time.sleep(1)