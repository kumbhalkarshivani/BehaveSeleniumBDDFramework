from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.TestBase import TestBase


class AccountsPage(TestBase):
    _ACCOUNT_SECTION_LIST = (By.CLASS_NAME, "myaccount-link-list")

    def __init__(self, driver):
        super().__init__(driver)

    def get_account_section_list(self):
        return self.get_element_text(self._ACCOUNT_SECTION_LIST).split("\n")

