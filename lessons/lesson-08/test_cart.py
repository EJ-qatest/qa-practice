
from playwright.sync_api import Page, expect
from conftest import login

def test_cart_shows_no_badge(logged_in_page: Page):
    badge = logged_in_page.locator("[data-test='shopping-cart-badge']")
    expect(badge).not_to_be_visible()

def test_cart_page_is_empty(logged_in_page: Page):
    logged_in_page.locator("[data-test='shopping-cart-link']").click()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(logged_in_page.locator("[data-test='title']")).to_have_text("Your Cart")

    cart_items = logged_in_page.locator("[data-test='inventory-item-name']")
    expect(cart_items).to_have_count(0)
