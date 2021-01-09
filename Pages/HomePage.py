from selenium.webdriver.common.by import By

from Pages.LoginPage import loginPage
from Pages.RegisterPage import registerPage


class homePage:
    MyAccount_xpath = (By.XPATH, "//span[text()='My Account']")

    Register_xpath = (By.XPATH, "//a[text()='Register']")

    Login_xpath = (By.XPATH, "//a[text()='Login']")

    def __init__(self, driver):

        self.driver = driver

    def openURL(self, url):
        self.driver.get(url)

    def clickMyAccount(self):
        self.driver.find_element(*homePage.MyAccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(*homePage.Register_xpath).click()

        self.rp = registerPage(self.driver)

        return self.rp

    def clickLogin(self):

        self.driver.find_element(*homePage.Login_xpath).click()

        self.lp = loginPage(self.driver)

        return self.lp
