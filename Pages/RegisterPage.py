from selenium.webdriver.common.by import By

from Pages.BasePage import basePage


class registerPage(basePage):

    __FirstName_css = (By.CSS_SELECTOR, "#input-firstname")

    __LastName_css = (By.CSS_SELECTOR, "#input-lastname")

    __Email_css = (By.CSS_SELECTOR, "#input-email")

    __Telephone_css = (By.CSS_SELECTOR, "#input-telephone")

    __Password_css = (By.CSS_SELECTOR, "#input-password")

    __ConfirmPassword_css = (By.CSS_SELECTOR, "#input-confirm")

    __PrivacyPolicy_name = (By.NAME, "agree")

    __Continue_xpath = (By.XPATH, "//input[@type='submit']")

    __ConfirmationMessage_xpath = (By.XPATH, "//div[@id='content']//h1")

    def __init__(self, driver):

        super().__init__(driver)

    def enterPersonalDetails(self, fname, lname, email, telephone):

        self.driver.find_element(*registerPage.__FirstName_css).send_keys(fname)

        self.driver.find_element(*registerPage.__LastName_css).send_keys(lname)

        self.driver.find_element(*registerPage.__Email_css).send_keys(email)

        self.driver.find_element(*registerPage.__Telephone_css).send_keys(telephone)

    def enterPassword(self, password):

        self.driver.find_element(*registerPage.__Password_css).send_keys(password)

        self.driver.find_element(*registerPage.__ConfirmPassword_css).send_keys(password)

    def clickButton(self):

        self.driver.find_element(*registerPage.__PrivacyPolicy_name).click()

        self.driver.find_element(*registerPage.__Continue_xpath).click()

    def verifyReister(self):

        return self.driver.find_element(*registerPage.__ConfirmationMessage_xpath).text
