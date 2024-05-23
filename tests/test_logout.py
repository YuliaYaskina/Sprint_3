import settings
from conftest import driver
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestLogout:
    def test_logout_from_lk(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_TITLE))
        assert driver.current_url == settings.URL_LOGIN

