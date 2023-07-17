from behave import *
from config.config import TestData
from pages.AccountsPage import AccountsPage
from pages.LoginPage import LoginPage
from pages.TestBase import TestBase


@given(u'user has already logged in to application')
def user_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_on_SignIn()

    for row in context.table:
        context.login_page.input_email(row["username"])
        context.login_page.input_password(row["password"])
        context.login_page.click_submit()


@then(u'user gets accounts section')
def user_on_accounts_page(context):
    context.account_page = AccountsPage(context.driver)
    context.actual_section_list = context.account_page.get_account_section_list()
    for item in context.table:
        assert item[0] in context.actual_section_list


@then(u'accounts section count should be "{size}"')
def step_impl(context, size):
    assert len(context.actual_section_list) == int(size)
