from PythonPrimerLogin.Locators.locators import Locator as loc

class TimesheetHome():
    def __init__(self, driver):
        self.driver=driver

        #Get locators:
        self.currentTimesheet_xpath=loc.currentTimesheet_xpath
        self.profile_class_name=loc.profile_class_name
        self.logoutButton_xpath=loc.logoutButton_xpath

    def switchToTimeCard(self):
        self.driver.find_element_by_xpath(self.currentTimesheet_xpath).click()

    def logout(self):
        self.driver.find_element_by_class_name(self.profile_class_name).click()
        self.driver.find_element_by_xpath(self.logoutButton_xpath).click()