
from playwright.sync_api import Page, expect
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


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
