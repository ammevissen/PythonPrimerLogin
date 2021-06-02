from Locators.locators import Locator as loc


class loginPage():

    def __init__(self, driver) -> None:
        self.driver=driver

        f = open("C:/Users/ammev/Desktop/Udemy Python Selenium/PythonPrimerLogin/LoginInfo.txt", "r")
        lines=[]
        for i in f.readlines():
            lines.append(i)

        userName=lines[0] #f.readlines()
        password=lines[1] #f.readlines()

        f.close()

    def login(self):

