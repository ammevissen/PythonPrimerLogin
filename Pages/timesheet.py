from PythonPrimerLogin.Locators.locators import Locator as loc

class Timesheet():
    def __init__(self, driver):
        self.driver=driver
    
        #Get locators:
        self.MTime_id=loc.MTime_id
        self.TTime_id=loc.TTime_id
        self.WTime_id=loc.WTime_id
        self.RTime_id=loc.RTime_id
        self.FTime_id=loc.FTime_id

        self.submitTimeButton_xpath=loc.submitTimeButton_xpath

    def enterTime(self):
        self.sendKeysById(self.MTime_id, 8)
        self.sendKeysById(self.TTime_id, 8)
        self.sendKeysById(self.WTime_id, 8)
        self.sendKeysById(self.RTime_id, 8)
        self.sendKeysById(self.FTime_id, 8)

    def sendKeysById(self, locator, keys):
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(keys)
        
    def submitTime(self):
        self.driver.find_element_by_xpath(self.submitTimeButton_xpath).click()