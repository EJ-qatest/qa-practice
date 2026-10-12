import pytest
from playwright.sync_api import Page, expect


def login(page: Page, username: str):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill(username)
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()


@pytest.fixture
def logged_in_page(page: Page):
    login(page, "standard_user")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    return page
