from behave.fixture import use_fixture_by_tag
from Utilities.DriverFactory import Driver
from Utilities.ConfigReader import readConfig


def before_scenario(context, scenario):

    driver = Driver.getDriver()

    context.driver = driver


def after_scenario(context, scenario):

    context.driver.close()
