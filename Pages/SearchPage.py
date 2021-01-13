import time

from selenium.webdriver.common.by import By

from Pages.BasePage import basePage


class searchPage(basePage):
    __SearchBox_name = (By.NAME, "search")

    __SearchButton_xpath = (By.XPATH, "//span[@class='input-group-btn']")

    __SearchedProduct_xpath = (By.XPATH, "//div[@class='caption']//h4//a")

    __PriceOfProduct_xpath = (By.XPATH, "//h2[text()='What would you like to do next?']//preceding::td[1]")

    __NoOfProduct_name = (By.NAME, "quantity")

    __AddCart_css = (By.CSS_SELECTOR, "#button-cart")

    __CartTotal_css = (By.CSS_SELECTOR, "#cart-total")

    __ViewCart_xpath = (By.XPATH, "//p[@class='text-right']//a[1]")

    __finalProductName_xpath = (By.XPATH, "//div[@id='content']//h1//following::tr//td[@class='text-left']//a")

    __finalPrice_xpath = (By.XPATH, "//a[text()='Checkout']//preceding::td[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def searchProduct(self, product):

        self.driver.find_element(*searchPage.__SearchBox_name).send_keys(product)

        self.driver.find_element(*searchPage.__SearchButton_xpath).click()

        productName = self.driver.find_element(*searchPage.__SearchedProduct_xpath).text

        self.driver.find_element(*searchPage.__SearchedProduct_xpath).click()

        return productName

    def addToCart(self, quantity):

        self.driver.find_element(*searchPage.__NoOfProduct_name).clear()

        self.driver.find_element(*searchPage.__NoOfProduct_name).send_keys(quantity)

        self.driver.find_element(*searchPage.__AddCart_css).click()

        time.sleep(2)

        self.driver.find_element(*searchPage.__CartTotal_css).click()

        time.sleep(2)

        self.driver.find_element(*searchPage.__ViewCart_xpath).click()

        time.sleep(5)

    def getFinalPrice(self):

        return self.driver.find_element(*searchPage.__finalPrice_xpath).text

    def getCartPrice(self):

        return self.driver.find_element(*searchPage.__PriceOfProduct_xpath).text

    def getFinalProductName(self):

        return self.driver.find_element(*searchPage.__finalProductName_xpath).text

