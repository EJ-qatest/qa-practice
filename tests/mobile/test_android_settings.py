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
