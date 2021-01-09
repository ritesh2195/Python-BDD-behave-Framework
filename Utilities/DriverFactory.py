from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities.ConfigReader import readConfig


class Driver:

    @staticmethod
    def getDriver():
        if readConfig.getBrowser() == "Chrome":

            driver = webdriver.Chrome(ChromeDriverManager().install())

            return driver

        elif readConfig.getBrowser() == "Firefox":

            driver = webdriver.Firefox(GeckoDriverManager().install())

            return driver
        else:

            return webdriver.Firefox(GeckoDriverManager().install())