# MOBILE-BUG-002: Cart - New user sees the previous user's cart items after login

| | |
|---|---|
| **App** | My Demo App (Android), emulator Pixel 8 Pro, Android 17 |
| **Users** | `bod@example.com` then `visual@example.com` |
| **Severity** | High - data privacy issue: one user can see (and check out) another user's cart |
| **Same bug on web?** | Yes - see [BUG-003](BUG-003-cart-shared-between-users.md) |

## Steps to reproduce
1. Log in as `bod@example.com`
2. Add **Sauce Labs Backpack** to the cart
3. Log out (menu -> Log Out -> LOGOUT)
4. Log in as `visual@example.com`
5. Open the cart

## Expected
The new user's cart is empty.

## Actual
`visual@example.com`'s cart shows bod's **Sauce Labs Backpack** ($29.99, 1 item), with **Proceed To Checkout** available.

## Evidence
- `evidence/MOBILE-BUG-002-1-bod-adds-backpack.png`
- `evidence/MOBILE-BUG-002-2-bod-logs-out.png`
- `evidence/MOBILE-BUG-002-3-visual-logged-in.png`
- `evidence/MOBILE-BUG-002-4-visual-cart-has-bods-backpack.png` - the bug
- Screen recording: Screen Recording 2026-11-19 at 7.35.51PM.mov
