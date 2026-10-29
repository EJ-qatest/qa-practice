
from playwright.sync_api import Page, expect
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage, ProductPage


def test_checkout_without_first_name_shows_error(page: Page):
    # 1. Log in
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    # 2. Add backpack and go to cart
    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    # 3. Check we're on the cart, then start checkout
    cart = CartPage(page)
    expect(cart.title).to_have_text("Your Cart")
    cart.start_checkout()

    # 4. Leave first name empty
    checkout = CheckoutPage(page)
    checkout.fill_details("", "Salivan", "94562")

    # 5. Check the error
    expect(checkout.error_message).to_contain_text("First Name is required")


def test_product_info(page: Page):
    # log in as standard_user
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")
    
    # click the backpack name
    inventory = InventoryPage(page)
    inventory.backpack_page()
    
    # prove you're on the details page
    product_page = ProductPage(page)
    expect(product_page.back_button).to_be_visible()
    # check the name is Sauce Labs Backpack
    
    expect(product_page.name).to_have_text("Sauce Labs Backpack")
    # check the price is $29.99
    expect(product_page.price).to_have_text("$29.99")
    
def test_continue_shopping_keeps_cart(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory=InventoryPage(page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(page)
    expect(cart.title).to_have_text("Your Cart")
    cart.continue_shopping()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory.cart_badge).to_have_text("1")
    expect(inventory.backpack_remove_button).to_have_text("Remove")
    
     

    
    

    
