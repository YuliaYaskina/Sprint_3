import settings
from conftest import driver
from locators import Locators
from data import ServiceTestData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestLk:
    def test_lk_from_main(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        assert driver.current_url == settings.URL_LK

    def test_from_lk_to_constructor(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_TITLE))
        assert driver.current_url == settings.URL

    def test_from_lk_to_logo(self,driver):
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(ServiceTestData.AUTH_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(ServiceTestData.AUTH_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_TITLE))
        assert driver.current_url == settings.URL




