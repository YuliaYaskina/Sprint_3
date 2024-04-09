from conftest import driver
from locators import Locators

class TestConstructor:
    def test_sauce(self,driver):
        driver.find_element(*Locators.SAUCE).click()
        assert driver.find_element(*Locators.SAUCE_PARENT)

    def test_stuffing(self,driver):
        driver.find_element(*Locators.STUFFING).click()
        assert driver.find_element(*Locators.STUFFING_PARENT)

    def test_roll(self,driver):
        driver.find_element(*Locators.SAUCE).click()
        driver.find_element(*Locators.ROLL).click()
        assert driver.find_element(*Locators.ROLL_PARENT)




