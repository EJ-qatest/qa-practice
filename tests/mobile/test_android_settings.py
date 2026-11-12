import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pages.android_settings import SettingsScreen 


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.android.settings"
    options.app_activity = ".Settings"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_open_network_settings(driver):
    settings = SettingsScreen(driver)
    settings.open_item("Network")
    assert settings.is_showing("Internet")

def test_open_display_settings(driver):
    settings = SettingsScreen(driver)
    settings.open_item("Display")
    assert settings.is_showing("Display size")

def test_open_accessibility_settings(driver):
    settings = SettingsScreen(driver)
    settings.scroll_to("Accessibility").click()
    assert settings.is_showing("TalkBack")

def test_open_sound_vibration_settings(driver):
    settings = SettingsScreen(driver)
    settings.open_item("Sound & vibration")
    assert settings.is_showing("Media volume")

"""#def test_search_settings(driver):
    # tap the search bar, found by its ID
    driver.find_element(AppiumBy.ID, "com.android.settings:id/search_bar_title").click()
    # find the text box (EditText) on the search screen
    search_box = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText") 
    # type "bright" into it
    search_box.send_keys("bright") 
    # check "Brightness" is showing in the results
    brightness = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Brightness")')
    assert brightness.is_displayed()"""

def test_search_settings(driver):
    settings = SettingsScreen(driver)
    settings.search("bright")
    #check "Brightness" is showing
    assert settings.is_showing("Brightness")


    
