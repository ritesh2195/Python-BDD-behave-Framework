from selenium.webdriver.common.by import By


class loginPage:

    __Email_css = (By.CSS_SELECTOR, "#input-email")

    __Password_css = (By.CSS_SELECTOR, "#input-password")

    __ForgetPassword_xpath = (By.XPATH, "//a[text()='Forgotten Password']")

    __LoginButton_xpath = (By.XPATH, "//input[@type='submit']")

    __EditAccount_xpath = (By.XPATH, "//a[text()='Edit your account information']")

    __ValidateEmail_xpath = (By.XPATH, "//input[@name='email']")

    def __init__(self, driver):

        self.driver = driver

    def doLogin(self, email, password):

        self.driver.find_element(*loginPage.__Email_css).send_keys(email)

        self.driver.find_element(*loginPage.__Password_css).send_keys(password)

    def clickLoginButton(self):

        self.driver.find_element(*loginPage.__LoginButton_xpath).click()

    def validateLogin(self):

        self.driver.find_element(*loginPage.__EditAccount_xpath).click()

        return self.driver.find_element(*loginPage.__ValidateEmail_xpath).get_attribute("value")
