# Confidence Round - Bug Hunt (Oct 29)
# This file has 6 bugs - all ones YOU have hit this week.
# Run it, read the error, fix ONE bug, run again. Repeat until 2 passed.
#   pytest lessons/lesson-09/bug_hunt.py -v
# (The file name doesn't start with test_ on purpose, so CI ignores it while it's broken.)

from playwright.sync_api import Page, expect
from pages import LoginPage, InventoryPage, CartPage


def test_add_backpack_shows_badge(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()
    expect(inventory.cart_badge).to_have_text("1")


def test_cart_keeps_backpack(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user")

    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    inventory.open_cart()
    cart = CartPage(page)
    expect(cart.title).to_have_text("Your Cart")

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.item_names).to_have_text("Sauce Labs Backpack")
