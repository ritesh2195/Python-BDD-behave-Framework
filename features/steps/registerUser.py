from behave import given, when, then
from Pages.HomePage import homePage
from Utilities.ConfigReader import readConfig
from Utilities.RandomData import *


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

    assert msg == "Your Account Has Been Created!"
