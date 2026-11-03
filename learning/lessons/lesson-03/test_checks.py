# Lesson 3: how things appear & disappear on screen
# Read it first. Guess what each line does. Then run it.

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # --- Part A: a blocked user ---
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("locked_out_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("locked out")

    # --- Part B: add and remove an item ---
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='login-button']").click()

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("1")

    page.locator("[data-test='remove-sauce-labs-backpack']").click()
    expect(badge).not_to_be_visible()

    browser.close()
