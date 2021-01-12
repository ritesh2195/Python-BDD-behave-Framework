from datetime import datetime

import allure
from behave import given, when, then
from Utilities.DriverFactory import Driver
from Pages.HomePage import homePage
from Pages.RegisterPage import registerPage
from Utilities.ConfigReader import readConfig
from Utilities.ConfigReader import readConfig
from Utilities.RandomData import *
from Utilities.captureScreenshot import *


@given(u'user navigate to home page')
def step_impl(context):
    context.hp = homePage(context.driver)

    context.hp.openURL(readConfig.getURL())


@given(u'user navigate to register page')
def step_impl(context):
    context.hp.clickMyAccount()

    context.rp = context.hp.clickRegister()


@given(u'user enter all required information')
def step_impl(context):
    context.rp.enterPersonalDetails(firstName(), lastName(), email(), telephone())

    context.rp.enterPassword(password())


@when(u'user click on privacy button and click to continue')
def step_impl(context):
    context.rp.clickButton()


@then(u'user should be able to signup into the application')
def step_impl(context):
    msg = context.rp.verifyReister()

    try:

        assert msg == "Your Account Has not Been Created!"

    except AssertionError as msg:

        takeScreenshot(context.driver)

        assert False
