import pytest
import time
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from pages.AddCustomer import AddCustomer
from utilities.readproperty import ReadProperty
import random
import string

class TestAddCustomer:
    baseURL= ReadProperty.getapplicationurl()
    username= ReadProperty.getusername()
    password= ReadProperty.getpassword()

    def random_email(self,char_num):
        random_email = ''
        for x in range(char_num):
                random_email+=''.join(random.choice(string.ascii_lowercase))

        return random_email

    def test_add_customer(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_login_button()
        self.cust=AddCustomer(self.driver)
        time.sleep(5)
        self.cust.clickOnCustomerMenu()
        self.cust.clickOnCustomerMenuItem()
        self.cust.clickonAddnew()
        self.email=self.random_email(7)+"@gmail.com"
        self.cust.setEmail(self.email)
        self.cust.setPassword("test123")
        self.cust.setFirstname("Rajani")
        self.cust.setLastname("Kota")
        self.cust.setGender("Female")
        self.cust.setDateOfBirth("09/20/1985")
        self.cust.setCompany("Wipro")
        self.cust.setCustomerRole("Guests")
        time.sleep(5)
        self.cust.setManagerOfVendor("Vendor 2")
        self.cust.setAdminComment("This is a test")
        self.driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(6)
        #self.cust.clickOnSave()
        self.btn=self.driver.find_element(By.XPATH,"//button[@name='save']")
        self.driver.execute_script("arguments[0].click();", self.btn)
       # message=self.driver.find_element(By.XPATH,"(//div[@class='alert alert-success alert-dismissable'])[1]").text
        #print(message)
        act_title=self.driver.title
        print(act_title)
        self.driver.close()
        #if act_title=="Customers / nopCommerce administration.":
            #assert True
        #else:
            #assert False







