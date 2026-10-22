import pytest
from playwright.sync_api import Page, expect


def login(page: Page, username: str):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill(username)
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()


def test_standard_user_can_add_bolt_tshirt(page: Page):
    login(page, "standard_user")
    page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


@pytest.mark.xfail(reason="BUG-002: Add to cart broken for some products (problem_user)")
def test_problem_user_can_add_bolt_tshirt(page: Page):
    login(page, "problem_user")
    page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
