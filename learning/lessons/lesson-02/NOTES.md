# Lesson 2 notes - selectors

## Big ideas
1. One element can have many "addresses" (selectors).
2. Find them: right-click the element -> **Inspect**.
3. Prefer `data-test` - it's made for testers and rarely changes.
4. Code matches text **exactly**: "Username" is not "user name".

## Selector cheat sheet
| In the HTML            | In Playwright                          |
|------------------------|----------------------------------------|
| `id="user-name"`       | `page.locator("#user-name")`  (# = id) |
| `class="shopping_cart_badge"` | `page.locator(".shopping_cart_badge")` (. = class) |
| `data-test="password"` | `page.locator("[data-test='password']")` |
| `placeholder="Username"` | `page.get_by_placeholder("Username")` |

## New code ideas
- `slow_mo=500` - pause 500 **milliseconds** (0.5 sec) before each action. 1000 ms = 1 sec.
- `badge = ...` - a **variable**: a name tag on something so you can use it later.
- `expect(badge).to_have_text("1")` - check the element shows exactly "1".
  Better than `assert` for pages: it **waits** (up to 5 sec) for the page to catch up.

## Run
```bash
python3 lessons/lesson-02/test_cart.py
```
