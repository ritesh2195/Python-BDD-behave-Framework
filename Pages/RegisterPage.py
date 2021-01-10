from selenium.webdriver.common.by import By

from Pages.BasePage import basePage


class registerPage(basePage):

    FirstName_css = (By.CSS_SELECTOR, "#input-firstname")

    LastName_css = (By.CSS_SELECTOR, "#input-lastname")

    Email_css = (By.CSS_SELECTOR, "#input-email")

    Telephone_css = (By.CSS_SELECTOR, "#input-telephone")

    Password_css = (By.CSS_SELECTOR, "#input-password")

    ConfirmPassword_css = (By.CSS_SELECTOR, "#input-confirm")

    PrivacyPolicy_name = (By.NAME, "agree")

    Continue_xpath = (By.XPATH, "//input[@type='submit']")

    ConfirmationMessage_xpath = (By.XPATH, "//div[@id='content']//h1")

    def __init__(self, driver):

        super().__init__(driver)

    def enterPersonalDetails(self, fname, lname, email, telephone):

        self.driver.find_element(*registerPage.FirstName_css).send_keys(fname)

        self.driver.find_element(*registerPage.LastName_css).send_keys(lname)

        self.driver.find_element(*registerPage.Email_css).send_keys(email)

        self.driver.find_element(*registerPage.Telephone_css).send_keys(telephone)

    def enterPassword(self, password):

        self.driver.find_element(*registerPage.Password_css).send_keys(password)

        self.driver.find_element(*registerPage.ConfirmPassword_css).send_keys(password)

    def clickButton(self):

        self.driver.find_element(*registerPage.PrivacyPolicy_name).click()

        self.driver.find_element(*registerPage.Continue_xpath).click()

    def verifyReister(self):

        return self.driver.find_element(*registerPage.ConfirmationMessage_xpath).text
