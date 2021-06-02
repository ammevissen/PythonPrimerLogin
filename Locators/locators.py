class Locator:
    #login
    username_id="37:2;a"
    password_id="47:2;a"
    loginButton_xpath="//button[contains(text(),'Log in')]"

    #timesheetHome:
    currentTimesheet_xpath="//button[contains(text(),'Open Current Timesheet')]"
    profile_class_name="profileName"
    logoutButton_xpath="//a[contains(text(),'Logout')]"

    #timesheet:
    MTime_id= "80:188;a" #"86:216;a"
    TTime_id= "92:188;a" #"92:216;a"
    WTime_id= "104:188;a" #"110:216;a"
    RTime_id= "116:188;a" #"122:216;a"
    FTime_id= "128:188;a"

    submitTimeButton_xpath="//button[contains(text(),'Submit')]"

