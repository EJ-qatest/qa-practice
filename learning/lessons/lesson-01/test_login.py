# Lesson 1: your first Playwright test
# Opens saucedemo.com, logs in, and CHECKS that login worked.
# Pattern of every test:  do some steps  ->  check what happened

from playwright.sync_api import sync_playwright   # bring in the Playwright tool

with sync_playwright() as p:                      # start Playwright, call it "p"; auto-cleanup at the end
    browser = p.chromium.launch(headless=False)   # open Chromium; headless=False = show the window
    page = browser.new_page()                     # open a new tab, call it "page"

    # --- DO: act like a user ---
    page.goto("https://www.saucedemo.com")        # go to the website
    page.fill("#user-name", "standard_user")      # type into the box with id "user-name"
    page.fill("#password", "secret_sauce")        # type into the password box
    page.click("#login-button")                   # click the login button

    # --- CHECK: act like a tester ---
    assert "inventory" in page.url, f"Login failed! Still on: {page.url}"
    browser.close()                               # close the browser
