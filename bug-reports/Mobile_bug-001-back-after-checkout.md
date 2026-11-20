# MOBILE-BUG-002: ____ - ____

| | |
|---|---|
| **App** | My Demo App (Android), emulator Pixel 8 Pro, Android 17 |
| **Users** | bod@example.com then visual@example.com |
| **Severity** | ____ high ____ |
| **Same bug on web?** | Yes - see BUG-003 |

## Steps to reproduce
1. Login on demo-app as bod@example.com user
2. Add product to cart
3. Logout from user account
4. Login as visual@example.com

## Expected
New user cart should be empty

## Actual
 User is still able to see product in the car


## Evidence
`evidence/MOBILE-BUG-002-____.png`