from Utilities.DriverFactory import Driver


def before_scenario(context, scenario):

    driver = Driver.getDriver()

    context.driver = driver


def after_scenario(context, scenario):

    context.driver.close()
