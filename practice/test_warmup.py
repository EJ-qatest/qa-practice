from playwright.sync_api import Page, expect


def test_login_works(page: Page):
    # 1. go to the saucedemo website
    page.goto("https://www.saucedemo.com/")
    # 2. fill in the username
    page.locator("[data-test='username']").fill("standard_user")
    # 3. fill in the password
    page.locator("[data-test='password']").fill("secret_sauce")
    # 4. click the login button
    page.locator("[data-test='login-button']").click()
    # 5. check the URL is the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
