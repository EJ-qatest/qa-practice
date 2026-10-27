# BUG-003: Cart - Items from one user's cart appear for the next user

| | |
|---|---|
| **App** | saucedemo.com |
| **Users** | `visual_user` then `standard_user` |
| **Severity** | High - one user can see another user's cart (privacy issue) |

## Steps to reproduce
1. Log in as `visual_user` (password `secret_sauce`)
2. Add **Sauce Labs Backpack** and **Sauce Labs Bike Light** to the cart
3. Check the cart badge shows **2**, then log out
4. Log in as `standard_user`

## Expected
The cart is completely empty, because this is a new and different user.

## Actual
Right after logging in, the cart badge shows **2**. Sauce Labs Backpack and Sauce Labs Bike Light show **Remove**.

`standard_user` can also check out and complete the order for these items (Item total $39.98, Total $43.18, then "Thank you for your order!"), even though they were added by `visual_user`.

## Evidence
Screen recording: Screen Recording 2026-10-27 at 11.32.20AM.mov (full flow: visual_user adds items, logs out, standard_user logs in and completes checkout)
