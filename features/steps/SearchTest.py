from behave import given, when, then

from Pages.HomePage import homePage
from Utilities.ConfigReader import readConfig
from Utilities.captureScreenshot import takeScreenshot


@given(u'user login into application')
def step_impl(context):
    context.hp = homePage(context.driver)

    context.hp.openURL(readConfig.getURL())

    context.hp.clickMyAccount()

    context.lp = context.hp.clickLogin()

    context.lp.doLogin(readConfig.getEmail(), readConfig.getPassword())

    context.sp = context.lp.clickLoginButton()


@given(u'user search "{product}" in search menu')
def step_impl(context, product):

    context.product = readConfig.getProduct()

    context.productName = context.sp.searchProduct(context.product)


@when(u'user add "{product}" in cart')
def step_impl(context, product):
    context.no = readConfig.getQuantity()

    context.initialPrice = context.sp.getPriceOfProduct()

    context.sp.addToCart(context.no)


@then(u'user should able to place order of that "{product}"')
def step_impl(context, product):

    finalProductName = context.sp.getFinalProductName()

    try:

        assert context.productName == finalProductName

    except AssertionError:

        takeScreenshot(context.driver)

        assert False
