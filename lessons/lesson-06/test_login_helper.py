# Lesson 6: write it once, use it everywhere (helper functions)
# Read it first. Guess. Then run it.

from playwright.sync_api import Page, expect


def login(page: Page, username: str):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill(username)
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()


def test_login_works(page: Page):
    login(page, "standard_user")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user_sees_error(page: Page):
    login(page, "locked_out_user")
    error = page.locator("[data-test='error']")
    expect(error).to_contain_text("locked out")


def test_remove_item_hides_badge(page: Page):
    login(page, "standard_user")
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("1")

    page.locator("[data-test='remove-sauce-labs-backpack']").click()
    expect(badge).not_to_be_visible()
