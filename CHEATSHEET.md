# QA Automation Cheat Sheet
Look things up here instead of memorizing. Nobody remembers code word for word.

---

## Start of every session
```bash
cd ~/qa-practice
source venv/bin/activate
```
Prompt should show `(venv) ... qa-practice %`

## Running tests
```bash
pytest lessons/lesson-08 -v                          # run a folder, list each test
pytest lessons/lesson-08 -v --headed --slowmo 500    # watch the browser
```
- **Check the COUNT**, not just green. A misnamed test (`check_...` instead of `test_...`) is silently skipped.
- **FAILED** = the test's check failed. **ERROR** = setup (a fixture) broke before the test started.
- **Unsaved file?** pytest runs what's SAVED. Look for the dot on the VS Code tab. Cmd+S.

---

## Lesson 6 - Helper function
**What:** steps written once, called by name.
**When:** the same steps appear in many tests.
```python
def login(page: Page, username: str):
    page.goto("https://www.saucedemo.com")
    page.locator("[data-test='username']").fill(username)
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

def test_locked_out(page: Page):
    login(page, "locked_out_user")      # "locked_out_user" fills the `username` slot
```
- Name doesn't start with `test_`, so pytest won't run it as a test.
- `username` (no quotes) = the variable. `"username"` (quotes) = the literal word.

---

## Lesson 7 - Fixture
**What:** setup pytest runs BEFORE a test, then hands the result to the test.
**When:** many tests need the same starting point (e.g. already logged in).
```python
import pytest

@pytest.fixture
def logged_in_page(page: Page):          # a fixture can ask for another fixture (page)
    login(page, "standard_user")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    return page                          # hand it to the test

def test_badge(logged_in_page: Page):    # ask for it by NAME in the parentheses
    ...
```
- Each test gets its OWN fresh run of the fixture (tests stay independent).
- **Don't** use it when login itself is what you're testing (login test, locked-out user, no password).

---

## Lesson 8 - conftest.py
**What:** a file named exactly `conftest.py`. Fixtures in it are available to EVERY test file in that folder.

| Thing | Shared automatically? |
|-------|----------------------|
| Fixtures (names in a test's parentheses) | YES - pytest finds them |
| Imports (`Page`, `expect`) | NO - every file needs its own |
| Helper functions (`login`) | NO - `from conftest import login` |

Every test file starts with:
```python
from playwright.sync_api import Page, expect
```

---

## Lesson 9 - Page Object
**What:** one class per page holding its selectors (with clear names) and actions.
**When:** the same selectors show up across many tests. Change a selector in ONE place.
```python
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.locator("[data-test='login-button']")
    def login(self, username, password="secret_sauce"):   # default value
        ...

def test_x(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", password="")         # override the default
```
- `self` = "this page object's own ..." (`self.login_button` = this login page's login button).

### Page Object RECIPE (structure never changes - only names + selectors do)
```python
class ____Page:                          # 1. page name + "Page"
    def __init__(self, page: Page):      # 2. ALWAYS this exact line
        self.page = page                 # 3. ALWAYS this exact line
        self.____ = page.locator("...")  # 4. one line per element (name = what it IS)

    def ____(self):                      # 5. one block per action (name = a VERB)
        self.____.click()                #    use the names from step 4, with self.
```
- Selectors = things (`cart_link`, `login_button`). Actions = verbs (`open_cart`, `login`). Never the same name for both.
- In a test: `cart = CartPage(page)` builds one. Inside the class, that same object is called `self`.


---

---

## Lesson 10 - API testing (no browser)
```python
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/users/1")              # Read
response = requests.post(f"{BASE_URL}/posts", json=data)    # Create
response = requests.put(f"{BASE_URL}/posts/1", json=data)   # Update
response = requests.delete(f"{BASE_URL}/posts/1")           # Delete

assert response.status_code == 200
user = response.json()            # server's JSON -> Python dictionary
assert user["name"] == "Leanne Graham"
assert "id" in created            # key exists (value chosen by server)
```
| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad request (you asked wrong) |
| 401/403 | Not logged in / not allowed |
| 404 | Not found |
| 500 | Server broke |

**Rule:** 2xx = good, 4xx = you asked wrong, 5xx = server broke.

**Dictionary** = labeled data, lives in a variable (NOT a file): `{"title": "Hi", "userId": 1}`. Read a value with `d["title"]`.
A JSON page in the browser is just the server's ANSWER - nothing is saved to your computer.

---

## Lesson 11 - Git (save points)
**Every session, at the end:**
```bash
git status                       # what changed? (red = not staged, green = staged)
git diff                         # exactly what changed (+ added, - removed). q to exit
git add .                        # stage everything (except .gitignore list)
git commit -m "what I did"       # seal the save point with a message
git log --oneline                # see history
```
- `.gitignore` lists what Git skips (venv/, __pycache__/, .DS_Store).
- **Git** = save points on your Mac. **GitHub** = online copy others can see.
- Commit messages say WHAT changed: "Add API tests for update + delete", not "stuff".

---

## Checks (expect)
| Check | Passes when |
|-------|-------------|
| `to_have_text("x")` | text is EXACTLY x |
| `to_contain_text("x")` | text INCLUDES x (skip decoration, keep meaning) |
| `to_be_visible()` / `not_to_be_visible()` | on screen / gone |
| `to_have_count(n)` | exactly n matching elements (waits + retries) |
| `expect(page).to_have_url("...")` | page address matches |

## Hard-won lessons
- A test only catches what you **check**. No `assert`/`expect` = no test. `print` never fails.
- **Container vs item:** `...-container` / `...-list` selectors grab the whole box, not one thing.
- **Timing:** after a click that changes pages, wait for something only on the NEW page (e.g. heading "Your Cart"), not just the URL. **Never** use fixed delays.
- **Empty list counts as "sorted".** Check the count too.
- `.click()` returns nothing - never save a click into a variable.
- **Failure messages only run when a check fails.** A wrong variable name inside `f"..."` hides until the worst moment. Re-read messages after renaming things.
