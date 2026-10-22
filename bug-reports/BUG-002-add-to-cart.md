# BUG-002: Inventory - "Add to cart" doesn't work for 3 products

| | |
|---|---|
| **App** | saucedemo.com |
| **User** | `problem_user` |
| **Works with `standard_user`?** | Yes |
| **Severity** | High - customers can't buy half of the catalog |

## Steps to reproduce
1. Log in as `problem_user` (password `secret_sauce`)
2. On the products page, click **Add to cart** on **Sauce Labs Bolt T-Shirt**

## Expected
The button changes to **Remove** and the cart badge increases.

## Actual
Nothing happens: the button still says **Add to cart** and the cart badge does not increase.

## Scope
| Product | Add to cart |
|---|---|
| Sauce Labs Backpack | Works |
| Sauce Labs Bike Light | Works |
| Sauce Labs Bolt T-Shirt | **Broken** |
| Sauce Labs Fleece Jacket | **Broken** |
| Sauce Labs Onesie | Works |
| Test.allTheThings() T-Shirt (Red) | **Broken** |
