from behave import *
from config.config import TestData
from pages.LoginPage import LoginPage
from pages.TestBase import TestBase


@given(u'user is on login page')
def open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_on_SignIn()


@when(u'user gets the title of the page')
def get_title(context):
    print(context.login_page.login_page_title())


@then(u'page title should be "{pagetitle}"')
def verify_page_title(context, pagetitle):
    assert context.login_page.login_page_title() == pagetitle


@then(u'forgot your password link should be displayed')
def verify_forgot_password_link(context):
    assert context.login_page.is_forget_password_link_exists()


@when(u'user enters username "{emailid}"')
def enter_username(context, emailid):
    context.login_page.input_email(emailid)


@when(u'user enters password "{password}"')
def step_impl(context, password):
    context.login_page.input_password(password)


@when(u'user clicks on Login button')
def step_impl(context):
    context.login_page.click_submit()


@then(u'user gets the title of the page')
def get_title(context):
    print(context.login_page.login_page_title())
