import settings
from conftest import driver
from locators import Locators
import time
from data import ServiceTestData

class TestLk:
    def test_lk_from_main(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        time.sleep(3)
        assert driver.current_url == settings.URL_LK

    def test_from_lk_to_constructor(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        time.sleep(3)
        assert driver.current_url == settings.URL

    def test_from_lk_to_logo(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        time.sleep(3)
        driver.find_element(*Locators.LOGO).click()
        time.sleep(3)
        assert driver.current_url == settings.URL




