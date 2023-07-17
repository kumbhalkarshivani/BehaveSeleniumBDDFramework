import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import TestData


def before_scenario(context, driver):

    if TestData.BROWSER == 'chrome':
        ser_object = Service(TestData.CHROME_EXECUTABLE_PATH)
        context.driver = webdriver.Chrome(service=ser_object)
    elif TestData.BROWSER == 'firefox':
        ser_object = Service(TestData.FIREFOX_EXECUTABLE_PATH)
        context.driver = webdriver.Firefox(service=ser_object)
    else:
        raise ValueError('Browser is not supported')
    context.driver.maximize_window()
    context.driver.get(TestData.URL)


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)
