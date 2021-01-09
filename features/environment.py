from behave.fixture import use_fixture_by_tag
from Utilities.DriverFactory import Driver
from Utilities.ConfigReader import readConfig


def before_scenario(context, scenario):

    if "login" in scenario.tags:

        driver = Driver.getDriver()

        driver.maximize_window()

        context.driver = driver

    elif "register" in scenario.tags:

        driver = Driver.getDriver()

        driver.maximize_window()

        context.driver = driver


def after_scenario(context, scenario):
    if "login" in scenario.tags:

        context.driver.close()

    elif "register" in scenario.tags:

        context.driver.close()
