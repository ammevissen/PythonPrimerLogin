from PythonPrimerLogin.Locators.locators import Locator as loc

class Timesheet():
    def __init__(self, driver):
        self.driver=driver
    
        #Get locators by Id:
        self.MTime_id=loc.MTime_id
        self.TTime_id=loc.TTime_id
        self.WTime_id=loc.WTime_id
        self.RTime_id=loc.RTime_id
        self.FTime_id=loc.FTime_id

        #Get locators by xpath:
        self.MTime_xpath=loc.MTime_xpathabs
        self.TTime_xpath=loc.TTime_xpathabs
        self.WTime_xpath=loc.WTime_xpathabs
        self.RTime_xpath=loc.RTime_xpathabs
        self.FTime_xpath=loc.FTime_xpathabs

        self.submitTimeButton_xpath=loc.submitTimeButton_xpath

    def enterTime(self):
        daysId=[self.MTime_id, self.TTime_id, self.WTime_id, self.RTime_id, self.FTime_id]
        daysXpath=[self.MTime_xpath, self.TTime_xpath, self.WTime_xpath, self.RTime_xpath, self.FTime_xpath]
        
        for day in range(len(daysId)):
            try:
                self.sendKeysById(daysId[day], 8)
            except:
                self.sendKeysByXpath(daysXpath[day], 8)

        # self.sendKeysById(self.MTime_id, 8)
        # self.sendKeysById(self.TTime_id, 8)
        # self.sendKeysById(self.WTime_id, 8)
        # self.sendKeysById(self.RTime_id, 8)
        # self.sendKeysById(self.FTime_id, 8)

    def sendKeysById(self, locator, keys):
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(keys)

    def sendKeysByXpath(self, locator, keys):
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(keys)
        
    def submitTime(self):
        self.driver.find_element_by_xpath(self.submitTimeButton_xpath).click()