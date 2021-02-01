from datetime import datetime

import allure

from Utilities.DriverFactory import Driver
from Utilities.captureScreenshot import takeScreenshot


def before_scenario(context, scenario):

    driver = Driver.getDriver()

    context.driver = driver


def after_scenario(context, scenario):

    if scenario.status == 'failed':

        takeScreenshot(context.driver)

    context.driver.close()
