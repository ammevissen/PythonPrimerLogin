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

        #Get locators:
        self.username_id=loc.username_id
        self.password_id=loc.password_id
        self.loginButton_xpath=loc.loginButton_xpath

    def login(self):
        self.sendKeysById(self.username_id, self.userName)
        self.sendKeysById(self.password_id, self.password)

    def sendKeysById(self, locator, keys):
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(keys)

    def click_login(self):
        self.driver.find_element_by_xpath(self.loginButton_xpath).click()

