# BUG-005: Inventory - 2 product titles and 1 button are misaligned

| | |
|---|---|
| **App** | saucedemo.com |
| **User** | `visual_user` |
| **Works with `standard_user`?** | Yes (everything aligned) |
| **Severity** | Low - cosmetic, doesn't stop anyone from buying |

## Steps to reproduce
1. Log in as `visual_user` (password `secret_sauce`)
2. Look at the product list

## Expected
All product titles and all "Add to cart" buttons are aligned the same way.

## Actual
- **Sauce Labs Bolt T-Shirt** and **Sauce Labs Fleece Jacket**: titles are shifted to the right compared with the other titles.
- **Test.allTheThings() T-Shirt (Red)**: the "Add to cart" button is shifted to the right compared with the other buttons.

## Evidence
- `evidence/BUG-005-visual-user-titles.png` - `visual_user`, misaligned titles and button
- `evidence/BUG-004-standard-user-prices.png` - `standard_user`, correct layout for comparison
