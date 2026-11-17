import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pages.mydemoapp import LoginScreen, ProductsScreen



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
    login_screen = LoginScreen(driver)
    login_screen.open()
    assert login_screen.is_open()
    login_screen.login("bod@example.com")
    products_screen = ProductsScreen(driver)
    assert products_screen.is_open()
   

def test_lockedout_user_sees_error(driver):
    login_screen = LoginScreen(driver)
    login_screen.open()
    assert login_screen.is_open()
    login_screen.login("alice@example.com")
    assert login_screen.locked_out()
    
    
    

    
    
   

    
