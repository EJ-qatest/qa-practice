# Lesson 9: tests that use Page Objects
# Read it first. Guess. Then run it.

from playwright.sync_api import Page, expect
from pages import LoginPage, InventoryPage, CheckoutPage, CartPage


def test_locked_out_user_sees_error(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user")
    expect(login_page.error_message).to_contain_text("locked out")


def test_login_with_no_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", password="")
    expect(login_page.error_message).to_contain_text("Password is required")


def test_add_backpack_shows_badge(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    expect(inventory.cart_badge).to_have_text("1")

def test_remove_backpack_hides_badge(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    expect(inventory.cart_badge).to_have_text("1")
    inventory.remove_backpack_from_cart()
    expect(inventory.cart_badge).not_to_be_visible()

def test_login_works(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_sort_price_low_to_high(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.sort_by("lohi")
    price_list = inventory.product_prices.all_inner_texts()

    numbers = []
    for price in price_list:
        number = float(price.replace("$", ""))
        numbers.append(number)
        
    assert len(numbers) == 6, f"Expected 6 prices, found {len(numbers)}"
    assert numbers == sorted(numbers), f"Prices not sorted low to high: {numbers}"

def test_sort_price_high_to_low(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.sort_by("hilo")
    price_list = inventory.product_prices.all_inner_texts()

    numbers = []
    for price in price_list:
        number = float(price.replace("$", ""))
        numbers.append(number)
        
    assert len(numbers) == 6, f"Expected 6 prices, found {len(numbers)}"
    assert numbers == sorted(numbers, reverse=True), f"Prices not sorted high to low: {numbers}"

def test_sort_name_z_to_a(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.sort_by("za")
    names_list = inventory.product_names.all_inner_texts()
    
    assert len(names_list) == 6, f"Expected 6 names, found {len(names_list)}"
    assert names_list == sorted(names_list, reverse=True), f"names not sorted Z to A: {names_list}"  

def test_checkout_backpack(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    expect(inventory.cart_badge).to_have_text("1")
    inventory.open_cart()

    cart = CartPage(page)
    expect(cart.title).to_have_text("Your Cart")
    cart.start_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_details("Tester1", "Salivan", "94562")
    checkout.finish_order()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
   
    
def test_logout_works(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.logout()
    expect(login_page.login_button).to_be_visible()

def test_cart_is_empty(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.open_cart()

    cart = CartPage(page)
    expect(cart.title).to_have_text("Your Cart")
    expect(cart.item_names).to_have_count(0)
    
    
    
    
    

    
    
    
    
