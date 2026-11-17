from appium.webdriver.common.appiumby import AppiumBy


class LoginScreen:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # tap the menu icon
        self.driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV").click()
        # tap "Log In" in the menu
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Log In")').click()


    def is_open(self):
        # return whether the login title (loginTV) is displayed
        login_title = self.driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV")
        return login_title.is_displayed()


    def login(self, username, password="10203040"):
        # type the username into nameET
        self.driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET").send_keys(username)
        # type the password into passwordET
        self.driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET").send_keys(password)
        # tap loginBtn
        self.driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn").click()

    def locked_out(self):
        #locked out error msg is displayed
        locked_out_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("locked out")')
        return locked_out_error.is_displayed()




class ProductsScreen:
    def __init__(self, driver):
        self.driver = driver

    def is_open(self):
        # return whether the products title (productTV) is displayed
        products_title = self.driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
        return products_title.is_displayed()

