from selenium.webdriver.common.by import By


class LoginPage:

    texbox_username_xpath="//input[@id='Email']"
    texbox_password_xpath="//input[@id='Password']"
    button_login_xpath= "//button[normalize-space()='Log in']"
    button_logout_xpath= "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.texbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.texbox_username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.texbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.texbox_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()


