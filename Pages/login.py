from PythonPrimerLogin.Locators.locators import Locator as loc


class LoginPage():

    def __init__(self, driver) -> None:
        self.driver=driver

        #Get login credentials:
        f = open("C:/Users/ammev/Desktop/Udemy Python Selenium/PythonPrimerLogin/LoginInfo.txt", "r")
        lines=[]
        for i in f.readlines():
            lines.append(i)

        self.userName=lines[0] #f.readlines()
        self.password=lines[1] #f.readlines()

        f.close()

        #Get locators by Id:
        self.username_id=loc.username_id
        self.password_id=loc.password_id

        #Get locators by xpath:
        self.username_xpath=loc.username_xpathabs
        self.password_xpath=loc.password_xpathabs

        self.loginButton_xpath=loc.loginButton_xpath

    def login(self):
        try:
            self.sendKeysById(self.username_id, self.userName)
        except:
            self.sendKeysByXpath(self.username_xpath, self.userName)

        try:
            self.sendKeysById(self.password_id, self.password)
        except:
            self.sendKeysByXpath(self.password_xpath, self.password)

    def sendKeysById(self, locator, keys):
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(keys)

    def sendKeysByXpath(self, locator, keys):
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(keys)

    def click_login(self):
        self.driver.find_element_by_xpath(self.loginButton_xpath).click()

