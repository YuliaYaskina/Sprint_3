import settings
from conftest import driver
from locators import Locators
import time

class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT_REG).send_keys('Юлия')
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys('yulia_yaskina_7_997@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys('123456')
        driver.find_element(*Locators.REGISTER_BUTTON_REG).click()
        time.sleep(3)
        assert driver.current_url == settings.URL_LOGIN

    def test_registration_incorrect_password(self, driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT_REG).send_keys('Имя')
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys('yulia_yaskina_7_171@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys('123')
        driver.find_element(*Locators.REGISTER_BUTTON_REG).click()
        assert driver.find_element(*Locators.INCORRECT_PASSWORD_REG)


