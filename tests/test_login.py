import settings
from conftest import driver
from locators import Locators
import time
from data import ServiceTestData

class TestLogIn:
    def test_login_from_main(self,driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        time.sleep(3)
        assert driver.current_url == settings.URL

    def test_login_from_lk_button(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        time.sleep(3)
        assert driver.current_url == settings.URL

    def test_login_from_sign_in_button_reg(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.SIGN_IN_BUTTON_REG).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        time.sleep(3)
        assert driver.current_url == settings.URL

    def test_login_from_reset_pass_button(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.RESET_PASS_BUTTON).click()
        driver.find_element(*Locators.SIGN_IN_BUTTON_REG).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        time.sleep(3)
        assert driver.current_url == settings.URL










