import settings
from conftest import driver
from locators import Locators
import time
from data import ServiceTestData
class TestLogout:
    def test_logout_from_lk(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        time.sleep(3)
        driver.find_element(*Locators.LOGOUT).click()
        time.sleep(3)
        assert driver.current_url == settings.URL_LOGIN

