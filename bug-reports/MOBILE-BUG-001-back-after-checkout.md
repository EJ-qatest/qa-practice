# MOBILE-BUG-001: Checkout - Back button after order completion allows placing the same order again

| | |
|---|---|
| **App** | My Demo App (Android), emulator Pixel 8 Pro, Android 17 |
| **User** | `bod@example.com` |
| **Severity** | High - customer can be charged twice for the same order |

## Steps to reproduce
1. Log in as `bod@example.com`
2. Add Sauce Labs Backpack to the cart
3. Check out (shipping + payment) and tap **Place Order**
4. On "Checkout Complete", press the Android **Back** button

## Expected
User should not be able to pay again or see the same products in the cart once the order is finished (the cart should be empty).

## Actual
Back returns to "Checkout - Review your order" with the same items and the **Place Order** button active. Tapping it places the same order again. The cart badge still shows the ordered items.

## Notes
- Tapping **Continue Shopping** clears the cart correctly.
- Closing and reopening the app clears the cart correctly.
- Only **Back** leaves the completed order in the cart.

## Evidence
- `evidence/MOBILE-BUG-001-1` to `-3`: cart still shows 3 after Checkout Complete, same items ordered again ($95.96)
- `evidence/MOBILE-BUG-001-4`: Checkout Complete, before Back
- `evidence/MOBILE-BUG-001-5`: after Back - "Review your order" with Place Order active again
- `evidence/MOBILE-BUG-001-6`: cart still holds items after emulator snapshot restore
