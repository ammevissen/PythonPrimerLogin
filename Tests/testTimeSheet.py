import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import HtmlTestRunner

#from PythonPrimerLogin.Locators.locators import Locator as loc
from PythonPrimerLogin.Pages.login import LoginPage
from PythonPrimerLogin.Pages.timesheetHome import TimesheetHome
from PythonPrimerLogin.Pages.timesheet import Timesheet 


class TimesheetTests(unittest.TestCase):

     @classmethod
     def setUpClass(cls) -> None:
          #Open Chrome
          cls.driver=webdriver.Chrome(ChromeDriverManager().install())

          cls.driver.implicitly_wait(10)
          cls.driver.maximize_window()

          #Go to the website:
          cls.driver.get("https://rev2.force.com/revature/s/login/?ec=302&startURL=%2Frevature%2Fs%2Ftimesheet")
          time.sleep(2)

     @classmethod
     def tearDownClass(cls) -> None:
          time.sleep(2)
          #Close browser
          #cls.driver.close()
          #cls.driver.quit()
          print("Test Complete")

     def test_submit_timesheet(self):
          #Login:
          login=LoginPage(self.driver)
          login.login() 
          login.click_login()
          time.sleep(2)

          #Enter Time:
          timeHome=TimesheetHome(self.driver)
          timeHome.switchToTimeCard()
          time.sleep(2)

          #fill in time (for a standard week):
          timesheetPage=Timesheet(self.driver)
          timesheetPage.enterTime()

          #Submit:
          #driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
          timesheetPage.submitTime()
          time.sleep(2)

          #Logout
          timeHome.logout()





if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/ammev/Desktop/Udemy Python Selenium/PythonPrimerLogin/PythonPrimerLogin/Reports"))
