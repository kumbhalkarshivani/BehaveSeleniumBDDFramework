from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.TestBase import TestBase
from selenium import webdriver


class ContactUsPage(TestBase):
    __CONTACT_LINK = (By.LINK_TEXT, "Contact us")
    __SEND_BUTTON = (By.ID, "submitMessage")
    __SELECT_OPTION = (By.XPATH, "//*[@id='id_contact']")
    __MESSAGE_BOX = (By.ID, "message")
    __ALERT_MSG = (By.CLASS_NAME, "alert alert-success")
    __FORM_ELEMENT = (By.CLASS_NAME, "contact-form-box")

    def __init__(self, driver):
        super().__init__(driver)
        self.form_element = None

    def click_on_contactus(self):
        self.click_element(self.__CONTACT_LINK)

    def click_on_send(self):
        self.click_element(self.__SEND_BUTTON)

    def select_subject_Heading(self, heading):
        self.form_element = self.driver.find_element(By.CLASS_NAME, "clearfix")
        subject_drop_down = self.form_element.find_element(By.XPATH, "//*[@id='id_contact']")
        drop_down = Select(subject_drop_down)
        drop_down.select_by_visible_text(heading)

    def enter_message(self, message):
        self.input_element(self.__MESSAGE_BOX, message)

    def get_message(self):
        return self.driver.find_element(By.XPATH, "//*[@id='center_column']/p").text
