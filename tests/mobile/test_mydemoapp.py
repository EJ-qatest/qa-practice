import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy



@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.saucelabs.mydemoapp.android"
    options.app_activity = ".view.activities.SplashActivity"
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_works(driver):
    # tap the menu icon (menuIV)
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV").click()
    # tap "Log In" in the menu (by text)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Log In")').click()

    # prove you're on the login screen (loginTV is displayed)
    login_title = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV")
    assert login_title.is_displayed()
    # type the username into nameET
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET").send_keys('bod@example.com')
    # type the password into passwordET
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET").send_keys('10203040')
    # tap loginBtn
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn").click()
    # check you landed on the right screen after login
    products_title = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    assert products_title.is_displayed()




    
