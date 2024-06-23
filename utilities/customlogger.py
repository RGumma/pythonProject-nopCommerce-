import logging

class CustomLogger:

    @staticmethod
    def Loggen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                 format='%(asctime)s:%(levelname)s %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger