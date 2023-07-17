from selenium.webdriver.common.by import By
from pages.TestBase import TestBase


class LoginPage(TestBase):
    SIGNIN_BUTTON = (By.LINK_TEXT, "Sign in")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot your password?")
    EMAILID = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    SUBMIT = (By.ID, "SubmitLogin")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_SignIn(self):
        self.click_element(self.SIGNIN_BUTTON)

    def login_page_title(self):
        return self.get_title()

    def is_forget_password_link_exists(self):
        return self.verify_element_displayed(self.FORGOT_PASSWORD_LINK)

    def input_email(self, email):
        self.input_element(self.EMAILID, email)

    def input_password(self, password):
        self.input_element(self.PASSWORD, password)

    def click_submit(self):
        self.click_element(self.SUBMIT)
