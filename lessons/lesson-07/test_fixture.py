# Lesson 7: fixtures - let pytest hand you a logged-in page
# Read it first. Guess. Then run it.

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    return page


def test_shop_shows_6_products(logged_in_page: Page):
    names = logged_in_page.locator("[data-test='inventory-item-name']")
    expect(names).to_have_count(6)


def test_add_to_cart_shows_badge(logged_in_page: Page):
    logged_in_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = logged_in_page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("1")
