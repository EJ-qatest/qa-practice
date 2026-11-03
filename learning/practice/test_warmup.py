import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
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

def test_get_post_one():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1


def test_add_backpack_shows_badge(logged_in_page: Page):
    logged_in_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = logged_in_page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("1")

def test_shows_6_products(logged_in_page: Page):
    names = logged_in_page.locator("[data-test='inventory-item-name']")
    expect(names).to_have_count(6)

    
