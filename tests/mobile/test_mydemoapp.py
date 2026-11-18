import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pages.mydemoapp import LoginScreen, ProductsScreen, ProductScreen, CartScreen, ShippingScreen, PaymentScreen, ReviewScreen, CompleteScreen



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


def checkout_one_product(driver):
    # log in as bod@example.com (LoginScreen: open, then login)
    login_screen = LoginScreen(driver)
    login_screen.open()
    assert login_screen.is_open()
    login_screen.login("bod@example.com")
    # open the first product, then add it to the cart
    products_screen = ProductsScreen(driver)
    products_screen.open_first_product()
    product = ProductScreen(driver)
    product.add_to_cart()
    # open the cart, then proceed to checkout
    products_screen.open_cart()
    cart = CartScreen(driver)
    cart.proceed_to_checkout()
    
    # prove the shipping screen is open, then fill the address (use your Rebecca T data)
    shipping = ShippingScreen(driver)
    assert shipping.is_open()
    shipping.fill_address('rebecca','214fsdkfndksj','Dumont', 'California', '98452','United States')
    # prove the payment screen is open, then fill the card
    payment = PaymentScreen(driver)
    assert payment.is_open()
    payment.fill_card('rebecae', '234523432423432', '05/29', '234')
    # place the order on the review screen
    review_screen = ReviewScreen(driver)
    assert review_screen.is_open()
    review_screen.place_order()
    # prove Checkout Complete is showing
    complete_screen = CompleteScreen(driver)
    assert complete_screen.is_open()

def test_checkout_completes(driver):
    # control: a normal checkout works
    checkout_one_product(driver)


@pytest.mark.xfail(raises=AssertionError, reason="MOBILE-BUG-001: Back after checkout allows placing the same order again")
def test_back_after_checkout_does_not_allow_reorder(driver):
    checkout_one_product(driver)
    # press the phone's Back button
    driver.back()
    # check the Review screen is NOT showing again
    review_screen = ReviewScreen(driver)
    assert not review_screen.is_open()
    

    
    
   

    
