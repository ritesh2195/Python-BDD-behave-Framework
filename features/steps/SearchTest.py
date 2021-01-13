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


@when(u'user add "{NoOfProduct}" in cart')
def step_impl(context, NoOfProduct):

    context.NoOfProduct = readConfig.getQuantity()

    context.sp.addToCart(context.NoOfProduct)


@then(u'user should able to place order of that "{product}"')
def step_impl(context, product):

    finalProductName = context.sp.getFinalProductName()

    cartPrice = context.sp.getCartPrice()

    finalPrice = context.sp.getFinalPrice()

    try:

        assert context.productName == finalProductName

        assert cartPrice == finalPrice

    except AssertionError:

        takeScreenshot(context.driver)

        assert False
