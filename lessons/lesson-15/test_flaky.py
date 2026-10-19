# Lesson 15: flaky tests - pass sometimes, fail sometimes
# Run 10 times:  pytest lessons/lesson-15 -v --count=10

import random

from playwright.sync_api import Page, expect


def test_simulated_slow_server():
    # SIMULATION: pretends the server sometimes answers too slowly.
    response_time = random.uniform(0.5, 1.5)
    assert response_time < 1.2, f"Server too slow: {response_time:.2f}s"


def test_cart_has_one_item(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='shopping-cart-link']").click()

    # Count the items in the cart
    badge = page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("1")

    
