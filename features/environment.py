import sys

import allure
from allure_commons.types import AttachmentType

from Utilities.DriverFactory import Driver
from datetime import datetime


def before_scenario(context, scenario):

    driver = Driver.getDriver()

    context.driver = driver


def after_scenario(context, scenario):

    context.driver.close()
