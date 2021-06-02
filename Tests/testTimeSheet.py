import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PythonPrimerLogin.Locators.locators import Locator as loc
from PythonPrimerLogin.Pages.login import LoginPage
from PythonPrimerLogin.Pages.timesheetHome import TimesheetHome
from PythonPrimerLogin.Pages.timesheet import Timesheet 

#getting login credentials  
f = open("C:/Users/ammev/Desktop/Udemy Python Selenium/PythonPrimerLogin/LoginInfo.txt", "r")
lines=[]
for i in f.readlines():
     lines.append(i)

userName=lines[0] #f.readlines()
password=lines[1] #f.readlines()

f.close()
# print(userName)
# print(password)

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()

#Go to the website:
driver.get("https://rev2.force.com/revature/s/login/?ec=302&startURL=%2Frevature%2Fs%2Ftimesheet")
#time.sleep(2)

#Login:
login=LoginPage(driver)
login.login()

# driver.find_element_by_id(loc.username_id).clear()
# driver.find_element_by_id(loc.username_id).send_keys(userName)

# driver.find_element_by_id(loc.password_id).clear()
# driver.find_element_by_id(loc.password_id).send_keys(password)

time.sleep(2)
#Enter Time: 
login.click_login()
#driver.find_element_by_xpath(loc.loginButton_xpath).click()

time.sleep(2)

#navigate to TimeSheet:
#driver.find_element_by_xpath("//button[contains(text(),'Open Current Timesheet')]").click()
#driver.find_element_by_xpath(loc.currentTimesheet_xpath).click()
timeHome=TimesheetHome(driver)
timeHome.switchToTimeCard()
time.sleep(2)

#fill in time (for a standard week):
#monday:
timesheetPage=Timesheet(driver)
timesheetPage.enterTime()

# LocatorM= "80:188;a" #"86:216;a"
# LocatorT= "92:188;a" #"92:216;a"
# LocatorW= "104:188;a" #"110:216;a"
# LocatorR= "116:188;a" #"122:216;a"
# LocatorF= "128:188;a" #"134:216;a"

# driver.find_element_by_id(LocatorM).clear()  
# driver.find_element_by_id(LocatorM).send_keys("8")

# #Tuesday:
# driver.find_element_by_id(LocatorT).clear()
# driver.find_element_by_id(LocatorT).send_keys("8")

# #Wednesday:
# driver.find_element_by_id(LocatorW).clear()
# driver.find_element_by_id(LocatorW).send_keys("8")

# #Thursday:
# driver.find_element_by_id(LocatorR).clear()
# driver.find_element_by_id(LocatorR).send_keys("8")

# #Friday:
# driver.find_element_by_id(LocatorF).clear()
# driver.find_element_by_id(LocatorF).send_keys("8")


#Comments:
# LocatorC="requesterComments"
# element= driver.find_element_by_name(LocatorC)
# element.clear()
# element.send_keys("Python Primer Timesheet Automation Test")
#xpath: "//textarea[contains(text(),'input')]
#name: "requesterComments"
#name: "requesterComments"
#class: "slds-textarea"
#id: input-  some number between 28 and 31
#tagName: "textarea" 
#//textarea[@id='input-31']

# driver.find_element_by_tag_name(LocatorC).clear()  
# driver.find_element_by_tag_name(LocatorC).send_keys("Python Primer Timesheet Automation Test") 

# driver.find_element_by_tag_name(LocatorC).clear()  
# driver.find_element_by_tag_name(LocatorC).send_keys("Python Primer Timesheet Automation Test") 
# driver.find_element_by_name(LocatorC).clear()  
# driver.find_element_by_name(LocatorC).send_keys("8")
# driver.find_element_by_name("requesterComments").clear()
# driver.find_element_by_name("requesterComments").send_keys("Python Primer Timesheet Automation Test")


# driver.find_element_by_css_selector("#input-31").clear()
#driver.find_element_by_css_selector("#input-31").send_keys("Python Primer Timesheet Automation Test")
#driver.find_element_by_class_name("slds-textarea").clear()
#driver.find_element_by_class_name("slds-textarea").send_keys("Python Primer Timesheet Automation Test")
#driver.find_element_by_id("input-31").send_keys("Python Primer Timesheet Automation Test")

time.sleep(2)
#Submit:
#driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
timesheetPage.submitTime()

time.sleep(2)
#Logout
timeHome.logout()
# driver.find_element_by_class_name("profileName").click()
# driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()


time.sleep(2)
#Close browser
driver.close()
driver.quit()
print("Test Complete")