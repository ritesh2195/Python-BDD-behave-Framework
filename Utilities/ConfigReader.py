import configparser

config = configparser.RawConfigParser()

config.read("D:\PYTHON\Ecommerce\Config\project.ini")


class readConfig:

    @staticmethod
    def getURL():
        return config.get('util', 'URL')

    @staticmethod
    def getBrowser():
        return config.get('Environment', 'Browser')
