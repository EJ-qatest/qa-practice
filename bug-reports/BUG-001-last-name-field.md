# BUG-001: Checkout - typed text doesn't stay in the Last Name field

| | |
|---|---|
| **App** | saucedemo.com |
| **User** | `problem_user` |
| **Works with `standard_user`?** | Yes |
| **Severity** | High - blocks checkout completely |
| **Evidence** | Screen recording (captured during exploratory testing) |

## Steps to reproduce
1. Log in as `problem_user` (password `secret_sauce`)
2. Add **Sauce Labs Backpack** to the cart
3. Open the cart and click **Checkout**
4. Click the **Last Name** field and type `Smith`

## Expected
`Smith` appears in the Last Name field.

## Actual
The Last Name field stays empty. The typed text does not stay in it, so the form can never be completed.
