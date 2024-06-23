import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:

#Add customer

    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAdd_new_xpath="//a[@class='btn btn-primary']"
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdGender_xpath="//input[@id='Gender_Male']"
    rdGender_Female_xpath="//input[@id='Gender_Female']"
    txtDoB_xpath="//input[@id='DateOfBirth']"
    txtCompanyName_xpath="//input[@id='Company']"
    lstCustRoles_xpath="(//ul[@class='select2-selection__rendered'])[2]"
    lst_itemAdministrators_xpath="//li[contains(text(),'Administrators')]"
    lst_itemRegistered_xpath="//li[contains(text(),'Registered')]"
    lst_itemGuest_xpath="//li[contains(text(),'Guests')]"
    lst_itemVendors_xpath="//li[contains(text(),'Vendors)]"
    drp_Manager_vendor_xpath="//select[@id='VendorId']"
    textAdmin_comment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAdd_new_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(companyname)

    def setDateOfBirth(self,dateofbirth):
        self.driver.find_element(By.XPATH, self.txtDoB_xpath).send_keys(dateofbirth)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH, self.textAdmin_comment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH, self.lstCustRoles_xpath).click()
        time.sleep(4)
        if role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lst_itemAdministrators_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lst_itemRegistered_xpath)
        elif role=='Guests':
            self.driver.find_element(By.XPATH,"//span[@role='presentation']").click()
            self.listitem=  self.driver.find_element(By.XPATH, self.lst_itemGuest_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lst_itemRegistered_xpath)
        elif role=='Vendors':
            self.listtem=self.driver.find_element(By.XPATH,self.lst_itemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lst_itemGuest_xpath)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drp_Manager_vendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.rdGender_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.rdGender_Female_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rdGender_xpath).send_keys(gender)

    def setFirstname(self,firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setCompany(self,company):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).click()

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH, self.textAdmin_comment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()



















