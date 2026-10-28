
# Lesson 9: Page Objects - each page's selectors and actions live in ONE place

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_box = page.locator("[data-test='username']")
        self.password_box = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str = "secret_sauce"):
        self.username_box.fill(username)
        self.password_box.fill(password)
        self.login_button.click()


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_names = page.locator("[data-test='inventory-item-name']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

        self.product_prices = page.locator("[data-test='inventory-item-price']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")
        self.backpack_link = page.locator("[data-test='item-4-title-link']")
        self.backpack_remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")

        
       
        

    def add_backpack_to_cart(self):
        self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    def remove_backpack_from_cart(self):
        self.page.locator("[data-test='remove-sauce-labs-backpack']").click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)
        
    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

    def add_bike_light_to_cart(self):
        self.page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()

# 
    def backpack_page(self):
        self.backpack_link.click()
        

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.item_names = page.locator("[data-test = 'inventory-item-name']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        
    def start_checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

   

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_box = page.locator("[data-test='firstName']")
        self.last_name_box = page.locator("[data-test='lastName']")
        self.postal_code_box = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator("[data-test='complete-header']")
        self.error_message = page.locator("[data-test='error']")
        self.cancel_button = page.locator("[data-test='cancel']")

    def fill_details(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_box.fill(first_name)
        self.last_name_box.fill(last_name)
        self.postal_code_box.fill(postal_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def cancel(self):
        self.cancel_button.click()



class ProductPage:

        
    def __init__(self, page: Page):
       
        self.page = page
        self.back_button = page.locator("[data-test='back-to-products']")
        self.name = page.locator("[data-test='inventory-item-name']")
        self.price = page.locator("[data-test='inventory-item-price']")
        self.description = page.locator("[data-test='inventory-item-desc']")
        self.add_to_cart_button = page.locator("[data-test='add-to-cart']")

    def add_to_cart(self):
        self.add_to_cart_button.click()
        
    def go_back(self):
        self.back_button.click()

         
        
        
          
        
        
