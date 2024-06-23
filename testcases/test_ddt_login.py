import time
import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from utilities.readproperty import ReadProperty
from utilities.customlogger import CustomLogger
from utilities import util


class TestDdtLogin:
    baseurl= ReadProperty.getapplicationurl()
    path= ".\\testdata\\LoginData.xlsx"


    def test_login_ddt(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.rows= util.getrowcount(self.path,'sheet1')
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user= util.readdata(self.path,'sheet1',r,1)
            self.passw=util.readdata(self.path,'sheet1',r,2)
            self.exp=util.readdata(self.path,'sheet1',r,3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.passw)
            self.lp.click_login_button()
            time.sleep(2)

            act_title= self.driver.title
            exp_title= 'Dashboard / nopCommerce administration'
            if act_title == exp_title:
                if self.exp=='pass':
                  self.lp.click_login_button()
                  lst_status.append("pass")

                elif self.exp=='fail':
                    self.lp.click_login_button()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp=='pass':
                    lst_status.append("fail")

                elif self.exp=='fail':
                    lst_status.append("pass")

        if 'fail' not in lst_status:
            print(" login DDT is passed")
            self.driver.close()
            assert True
        else:
            print(" login DDT is NOT passed")
            self.driver.close()
            assert False














