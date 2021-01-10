from selenium.webdriver.common.by import By

from Pages.BasePage import basePage
from Pages.LoginPage import loginPage
from Pages.RegisterPage import registerPage


class homePage(basePage):
    __MyAccount_xpath = (By.XPATH, "//span[text()='My Account']")

    __Register_xpath = (By.XPATH, "//a[text()='Register']")

    __Login_xpath = (By.XPATH, "//a[text()='Login']")

    def __init__(self, driver):

        super().__init__(driver)

    def openURL(self, url):
        self.driver.get(url)

    def clickMyAccount(self):
        self.driver.find_element(*homePage.__MyAccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(*homePage.__Register_xpath).click()

        self.rp = registerPage(self.driver)

        return self.rp

    def clickLogin(self):

        self.driver.find_element(*homePage.__Login_xpath).click()

        self.lp = loginPage(self.driver)

        return self.lp
