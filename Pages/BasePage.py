from Pages.Page import page
from selenium.webdriver.support import expected_conditions as ec


class basePage(page):

    def __init__(self, driver):
        super().__init__(driver)

    def getTitle(self):
        return self.driver.title

    def elementToClickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def waitForElementPresent(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))
