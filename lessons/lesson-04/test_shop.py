# Lesson 4: pytest - many small, independent tests
# Read it first. Guess. Then run it.

from playwright.sync_api import Page, expect


def test_login_works(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user_sees_error(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("locked_out_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    error = page.locator("[data-test='error']")
    expect(error).to_contain_text("locked out")


def test_remove_item_hides_badge(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("1")

    page.locator("[data-test='remove-sauce-labs-backpack']").click()
    expect(badge).not_to_be_visible()

def test_login_with_no_password(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='login-button']").click()

    error = page.locator("[data-test='error']")
    expect(error).to_contain_text("Password is required")

def test_logout_works(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator('#react-burger-menu-btn').click()
    page.locator("[data-test='logout-sidebar-link']").click()

    expect(page).to_have_url("https://www.saucedemo.com/")
    login_button = page.locator("[data-test='login-button']")
    expect(login_button).to_have_text('Login')

def test_sort_price_low_to_high(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("[data-test='product-sort-container']").select_option("lohi")
    price_list = page.locator("[data-test='inventory-item-price']").all_inner_texts()

    numbers = []
    for price in price_list:
        number = float(price.replace("$", ""))
        numbers.append(number)
        
    assert len(numbers) == 6, f"Expected 6 prices, found {len(numbers)}"
    assert numbers == sorted(numbers), f"Prices not sorted low to high: {numbers}"

def test_sort_price_high_to_low(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("[data-test='product-sort-container']").select_option("hilo")
    price_list = page.locator("[data-test='inventory-item-price']").all_inner_texts()

    numbers = []
    for price in price_list:
        number = float(price.replace("$", ""))
        numbers.append(number)
        
    assert len(numbers) == 6, f"Expected 6 prices, found {len(numbers)}"
    assert numbers == sorted(numbers, reverse=True), f"Prices not sorted high to low: {numbers}"



def test_sort_name_z_to_a(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.locator("[data-test='product-sort-container']").select_option("za")
    
    names  = page.locator("[data-test='inventory-item-name']").all_inner_texts()  

    assert len(names) == 6, f"Expected 6 names, found {len(names)}"
    assert names == sorted(names, reverse=True), f"names not sorted Z to A: {names}"  
    
def test_checkout_backpack(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge = page.locator("[data-test='shopping-cart-badge']")
    expect(badge).to_have_text("1")

    page.locator("[data-test='shopping-cart-link']").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator("[data-test='title']")).to_have_text("Your Cart")
    item_name = page.locator("[data-test='inventory-item-name']")
    expect(item_name).to_have_text("Sauce Labs Backpack")

    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Tester1")
    page.locator("[data-test='lastName']").fill("Salivan")
    page.locator("[data-test='postalCode']").fill("94562")
    page.locator("[data-test='continue']").click()

    page.locator("[data-test='finish']").click()
    thank_you = page.locator("[data-test='complete-header']")            
    expect(thank_you).to_have_text("Thank you for your order!")


    
    

    



