from pages.LoginPage import LoginPage
from selenium import webdriver
import pytest
from utilities.readproperty import ReadProperty
from utilities.customlogger import CustomLogger

class TestLogin:
    baseurl = ReadProperty.getapplicationurl()
    username = ReadProperty.getusername()
    password = ReadProperty.getpassword()

    log=CustomLogger.Loggen()

    def test_home_page(self,setup):
        self.driver=setup
        self.log.info("******TestLogin*****")
        self.log.info("******verifying the title*****")
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        act_title=self.driver.title
        if act_title=='Your store. Login':
            assert True
            self.log.info("*******Home page title is passed******")
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_home_page.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp= LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login_button()
        act_title=self.driver.title
        if act_title=='Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_login.png")
            self.driver.close()
            assert False





