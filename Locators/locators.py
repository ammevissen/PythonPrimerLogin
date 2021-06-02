class Locator:
    #login
    username_id="37:2;a"
    password_id="47:2;a"
    username_xpathabs="/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    password_xpathabs="/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]"
    loginButton_xpath="//button[contains(text(),'Log in')]"

    #timesheetHome:
    currentTimesheet_xpath="//button[contains(text(),'Open Current Timesheet')]"
    profile_class_name="profileName"
    logoutButton_xpath="//a[contains(text(),'Logout')]"

    #timesheet:
    "fullscreen values"
    MTime_id="80:188;a"
    TTime_id="92:188;a"
    WTime_id="104:188;a"
    RTime_id="116:188;a"
    FTime_id="128:188;a"

    MTime_xpathabs="/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/input[1]"
    TTime_xpathabs="/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/input[1]"
    WTime_xpathabs="/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/input[1]"
    RTime_xpathabs="/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/input[1]"
    FTime_xpathabs="/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]/input[1]"

    comment="/html[1]/body[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/input[1]"

    submitTimeButton_xpath="//button[contains(text(),'Submit')]"

