# Lesson 2: selectors - how a test finds things on a page
# Read it first. Guess what each line does. Then run it.

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("#login-button").click()

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()

    badge = page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("2")

    browser.close()
