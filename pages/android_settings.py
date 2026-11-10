from appium.webdriver.common.appiumby import AppiumBy


class SettingsScreen:
    def __init__(self, driver):
        self.driver = driver

    def find_text(self, text):
        # the long line lives here now, written only once
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')

    def open_item(self, text):
        self.find_text(text).click()

    def is_showing(self, text):
        return self.find_text(text).is_displayed()


    def scroll_to(self, text):
        # tells Android: "scroll the list until this text is on screen"
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("{text}"))'
        )
