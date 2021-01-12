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

    @staticmethod
    def getEmail():

        return config.get('util', 'email')

    @staticmethod
    def getPassword():

        return config.get('util', 'password')

    @staticmethod
    def getProduct():

        return config.get('util', 'product')
    @staticmethod
    def getQuantity():

        return config.get('util', 'quantity')
