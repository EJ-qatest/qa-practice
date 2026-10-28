# BUG-004: Inventory - Product list shows random prices that change on every login

| | |
|---|---|
| **App** | saucedemo.com |
| **User** | `visual_user` |
| **Works with `standard_user`?** | Yes (correct prices) |
| **Severity** | High - customer sees one price but is charged another |

## Steps to reproduce
1. Log in as `visual_user` (password `secret_sauce`)
2. Note the **Sauce Labs Backpack** price on the product list
3. Click **Add to cart**, then open the cart and go to checkout
4. Log out, log in again as `visual_user`, and check the price again

## Expected
The Backpack price is **$29.99** everywhere: product list, cart and checkout.

## Actual
The product list shows a random price that changes on every login. The cart and checkout use the real price.

| Where | Backpack price |
|---|---|
| Product list (login 1) | $23.81 |
| Product list (login 2) | $34.23 |
| Cart | $29.99 |
| Checkout overview | $29.99 (Total $32.39 with tax) |

The customer is charged $29.99 + tax, not the price shown on the product list.

## Scope
All products are affected, not only the Backpack (login 2):

| Product | Shown on list | Real price |
|---|---|---|
| Sauce Labs Backpack | $34.23 | $29.99 |
| Sauce Labs Bike Light | $78.97 | $9.99 |
| Sauce Labs Bolt T-Shirt | $95.49 | $15.99 |
| Sauce Labs Fleece Jacket | $5.38 | $49.99 |

## Evidence
- `evidence/BUG-004-list-login1.png` - product list, Backpack $23.81
- `evidence/BUG-004-cart.png` - cart, Backpack $29.99
- `evidence/BUG-004-checkout.png` - checkout overview, $29.99 (Total $32.39)
- `evidence/BUG-004-list-login2.png` - product list after logging in again, Backpack $34.23 and other products
- `evidence/BUG-004-standard-user-prices.png` - same page as `standard_user`, showing the real prices
