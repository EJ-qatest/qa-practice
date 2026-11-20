from appium.webdriver.common.appiumby import AppiumBy
PKG = "com.saucelabs.mydemoapp.android:id/"


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

    # add these 2 methods inside your existing ProductsScreen:
    def open_first_product(self):
        # tap the first product image (productIV)
        self.driver.find_element(AppiumBy.ID, f"{PKG}productIV").click()

    def open_cart(self):
        # tap the cart icon (cartIV)
        self.driver.find_element(AppiumBy.ID, f"{PKG}cartIV").click()
    def cart_badge(self):
        badge = self.driver.find_element(AppiumBy.ID, f"{PKG}cartTV")
        return badge.text        # gives back what it shows, like "3"


class ProductScreen:
    def __init__(self, driver):
        self.driver = driver
        

    def add_to_cart(self):
        self.driver.find_element(AppiumBy.ID, f"{PKG}cartBt").click()

    def tap_plus(self, times):
        for i in range(times):
            self.driver.find_element(AppiumBy.ID, f"{PKG}plusIV").click()
        


class CartScreen:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        # tap cartBt
        self.driver.find_element(AppiumBy.ID, f"{PKG}cartBt").click()


class ShippingScreen:
    def __init__(self, driver):
        self.driver = driver

    def is_open(self):
        # return whether checkoutTitleTV is displayed
        shipping_screen = self.driver.find_element(AppiumBy.ID, f"{PKG}checkoutTitleTV")
        return shipping_screen.is_displayed()
    

    def fill_address(self, name, address, city, state, zip_code, country):
        # type into fullNameET, address1ET, cityET, stateET, zipET, countryET
        self.driver.find_element(AppiumBy.ID, f"{PKG}fullNameET").send_keys(name)
        self.driver.find_element(AppiumBy.ID, f"{PKG}address1ET").send_keys(address)
        self.driver.find_element(AppiumBy.ID, f"{PKG}cityET").send_keys(city)
        self.driver.find_element(AppiumBy.ID, f"{PKG}stateET").send_keys(state)
        self.driver.find_element(AppiumBy.ID, f"{PKG}zipET").send_keys(zip_code)
        self.driver.find_element(AppiumBy.ID, f"{PKG}countryET").send_keys(country)
         # tap paymentBtn ("To Payment")
        self.driver.find_element(AppiumBy.ID, f"{PKG}paymentBtn").click()


class PaymentScreen:
    def __init__(self, driver):
        self.driver = driver

    def is_open(self):
        # return whether enterPaymentTitleTV is displayed
        payment_title = self.driver.find_element(AppiumBy.ID, f"{PKG}enterPaymentTitleTV")
        return payment_title.is_displayed()
    

    def fill_card(self, name, number, expiry, cvv):
        # type into nameET, cardNumberET, expirationDateET, securityCodeET
        self.driver.find_element(AppiumBy.ID, f"{PKG}nameET").send_keys(name)
        self.driver.find_element(AppiumBy.ID, f"{PKG}cardNumberET").send_keys(number)
        self.driver.find_element(AppiumBy.ID, f"{PKG}expirationDateET").send_keys(expiry)
        self.driver.find_element(AppiumBy.ID, f"{PKG}securityCodeET").send_keys(cvv)
        # tap paymentBtn ("Review Order")
        self.driver.find_element(AppiumBy.ID, f"{PKG}paymentBtn").click()

class ReviewScreen:
    def __init__(self, driver):
        self.driver = driver

    def place_order(self):
        # tap paymentBtn ("Place Order")
        self.driver.find_element(AppiumBy.ID, f"{PKG}paymentBtn").click()

    def is_open(self):
        found = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Review your order")')
        return len(found) > 0


class CompleteScreen:
    def __init__(self, driver):
        self.driver = driver

    def is_open(self):
        # return whether "Checkout Complete" text is displayed (textContains)
        checkout_complete = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Checkout Complete")')
        return checkout_complete.is_displayed()

