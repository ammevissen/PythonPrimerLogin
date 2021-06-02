f = open("C:/Users/ammev/Desktop/Udemy Python Selenium/PythonPrimerLogin/LoginInfo.txt", "r")

lines=[]
for i in f.readlines():
     lines.append(i)

userName=lines[0] #f.readlines()
password=lines[1] #f.readlines()

f.close()
print(userName)
print(password)