from datetime import datetime
import allure


def takeScreenshot(driver):
    currTime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    screenshotName = 'test' + '_' + currTime

    allure.attach(driver.get_screenshot_as_png(), name=screenshotName,
                  attachment_type=allure.attachment_type.PNG)
    driver.get_screenshot_as_file('D:\\PYTHON\Ecommerce\\screenshots\\' + screenshotName + '.png')