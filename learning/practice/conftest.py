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
