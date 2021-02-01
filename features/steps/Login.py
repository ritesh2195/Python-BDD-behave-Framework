from behave import given, when, then
from Pages.HomePage import homePage
from Utilities.ConfigReader import readConfig


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

    assert context.lp.verifyPageTitle() == 'My Account'

    mail = context.lp.validateLogin()

    assert mail == context.email
