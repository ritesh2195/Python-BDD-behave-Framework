import time

from behave import given, when, then

from Pages.HomePage import homePage
from Utilities.ConfigReader import readConfig
from Utilities.captureScreenshot import takeScreenshot


@given(u'user navigate to login page')
def step_impl(context):

    context.hp = homePage(context.driver)

    context.hp.openURL(readConfig.getURL())

    context.hp.clickMyAccount()

    context.lp = context.hp.clickLogin()


@given(u'user enter valid "{email}" and "{password}"')
def step_impl(context, email, password):

    context.lp.doLogin(email, password)

    context.email = email


@when(u'user click on the login button')
def step_impl(context):

    context.lp.clickLoginButton()


@then(u'user should be able login successfully')
def step_impl(context):

    try:

        mail = context.lp.validateLogin()

        assert mail == context.email

    except AssertionError as msg:

        takeScreenshot(context.driver)

        assert False

