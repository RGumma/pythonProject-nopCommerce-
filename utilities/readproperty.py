import configparser

config = configparser.ConfigParser()
config.read(".\\configuration\\config.ini")

class ReadProperty:

    @staticmethod
    def getapplicationurl():
        baseurl=config.get('common info', 'baseurl')
        return baseurl

    @staticmethod
    def getusername():
        username=config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('common info', 'password')
        return password



