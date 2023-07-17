from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import TestData

"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pages"""


class TestBase:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
        except EX as e:
            print("Exception! Can't click on the element")

    def input_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except EX as e:
            print("Exception! Can't click on the element")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def select_option(self, by_locator, option):
        try:
            self.driver.execute_script("window.scrollBy(0,350)", "")
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
            drop_down = Select(element)
            drop_down.select_by_visible_text(option)
        except ElementNotVisibleException:
            return False

    @staticmethod
    def launch_browser():
        if TestData.BROWSER == 'chrome':
            ser_object = Service(TestData.CHROME_EXECUTABLE_PATH)
            driver = webdriver.Chrome(service=ser_object)
        elif TestData.BROWSER == 'firefox':
            ser_object = Service(TestData.FIREFOX_EXECUTABLE_PATH)
            driver = webdriver.Firefox(service=ser_object)
        else:
            raise ValueError('Browser is not supported')
        driver.maximize_window()
        return driver
