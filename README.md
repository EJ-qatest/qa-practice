# QA Automation Practice

![Tests](https://github.com/EJ-qatest/qa-practice/actions/workflows/tests.yml/badge.svg)

## About me

I'm a QA engineer with 6 years of manual testing experience across web, iOS, and Android apps, plus some hardware testing.
I'm now building my automation skills, and this repo is where I practice: turning the test cases I'd normally run by hand
into reliable, automated tests that run on every code change.

## At a glance

| | |
|---|---|
| **Web UI tests** | 24 (Playwright + Page Object Model) |
| **API tests** | 7 (`requests`, full CRUD + negative cases) |
| **Android tests** | 10 (Appium + UiAutomator2, Page Object Model) on a demo shopping app and the Settings app |
| **Known-bug tests** | 3 (2 web, 1 mobile), each paired with a passing control test |
| **Bug reports** | 7 bugs (5 web, 2 mobile) + 2 requirements questions, with screenshot evidence |
| **CI** | Every push runs the suite on GitHub Actions, with an HTML report and failure screenshots |

## What's in this repo

```
pages/          Page Objects - one file per app, one class per page/screen
                  saucedemo.py (web), mydemoapp.py + android_settings.py (Android)
tests/web/      UI tests for an e-commerce demo site (saucedemo.com)
tests/api/      API tests against a public REST API (jsonplaceholder.typicode.com)
tests/mobile/   Android tests: Sauce Labs My Demo App + the Settings app (run locally on an emulator)
bug-reports/    Bug reports and requirements questions from exploratory testing, plus evidence/
learning/       My learning path: lessons and solo practice (not part of the test suite)
pytest.ini      Tells pytest where the tests live, so `pytest` runs the whole suite
```

### What the web tests cover

| Area | Examples |
|---|---|
| Login | Valid login, locked-out user, missing password |
| Cart | Add/remove items, badge count, empty cart |
| Sorting | Price low-high, high-low, name Z-A |
| Product details | Correct name, price and description |
| Navigation | Back to products, Continue Shopping and both Cancel buttons all keep the cart |
| Checkout | Full order, missing first name shows an error |

### What the Android tests cover

| Area | Examples |
|---|---|
| Login | Valid login, locked-out user sees an error |
| Checkout (end to end) | Product -> cart -> shipping -> payment -> review -> order complete, across 8 screens |
| Navigation | Menus, scrolling to items below the fold, the phone's Back button |
| Search | Tap a field by ID, type, check the results |

Locators were found with **Appium Inspector** (resource-ids, text, element types). Screens that reuse the same button ID are always confirmed by their title before tapping.

## Bugs I found

I explored the app by hand first, like I would on a real project, and wrote up what I found.

| Report | Issue | Severity | Automated? |
|---|---|---|---|
| [BUG-001](bug-reports/BUG-001-last-name-field.md) | Typed text doesn't stay in the Last Name field at checkout (`problem_user`) | High | - |
| [BUG-002](bug-reports/BUG-002-add-to-cart.md) | "Add to cart" doesn't work for 3 products (`problem_user`) | High | - |
| [BUG-003](bug-reports/BUG-003-cart-shared-between-users.md) | Cart is shared between users on the same browser, and the next user can check out with it | High | Yes |
| [BUG-004](bug-reports/BUG-004-random-prices-visual-user.md) | Product list shows random prices; checkout charges the real price | High | Yes |
| [BUG-005](bug-reports/BUG-005-misaligned-titles.md) | Product titles and a button are misaligned (`visual_user`) | Low | - |
| [MOBILE-BUG-001](bug-reports/MOBILE-BUG-001-back-after-checkout.md) | Android: pressing Back after "Checkout Complete" lets the user place the same order again | High | Yes |
| [MOBILE-BUG-002](bug-reports/MOBILE-BUG-002-cart-shared-between-users.md) | Android: a new user sees the previous user's cart (same bug as BUG-003 on web) | High | - |
| [QUESTION-001](bug-reports/QUESTION-001-quantity.md) | Can a customer order more than one of the same product? | - | - |
| [QUESTION-002](bug-reports/QUESTION-002-red-tshirt-name.md) | Is "Test.allTheThings()" meant to be part of a product name? | - | - |

### How known bugs are tracked in code

Each automated bug has two tests:

- A **control test** that passes for a normal user, which proves the check itself is correct.
- A **known-bug test** marked `xfail` with the bug number. It shows as "expected failure" today, and flips to `XPASS` the day the bug is fixed, so the suite tells us when to close the report.

I use `xfail(raises=AssertionError)`, so only a failed check counts as the expected failure. A typo or crash shows as a real failure instead of hiding behind the bug.

## Tech stack

Python · Playwright · Appium (UiAutomator2) · Android Studio emulator · pytest · requests · Git · GitHub Actions

## My test strategy

- **Unhappy paths matter as much as happy ones.** Alongside "login works", I test what should *fail*: a locked-out user, a missing password, a request for a user that doesn't exist (404).
- **Check the middle, not just the end.** In the checkout test I confirm the cart badge and the cart contents before checking out, so a failure points straight to the step that broke.
- **Checks should be strict where it matters and flexible where it doesn't.** I match exact text for prices and headings, but use "contains" for messages whose wording may change, so tests don't break for harmless reasons.
- **Wait for the right thing, never for a fixed time.** Tests wait for the new page's content to appear instead of using sleeps, which keeps them fast and avoids flaky failures.
- **"Not visible" checks need the page loaded first.** A check that something is *missing* passes instantly on a half-loaded page, so I first wait for something that *should* be there.
- **Don't trust a pass I can't explain.** When a known-bug test unexpectedly passed, I watched it run with `--headed --slowmo`, found the check was running too early, and fixed the test rather than the result.
- **Every test is independent.** Each one starts with a fresh browser and its own login, so one failure never hides or causes another.

## How to run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest -v --ignore=tests/mobile                # web + API suite (what CI runs)
pytest tests/web -v --headed --slowmo 500      # watch the browser while UI tests run
pytest -k cancel -v                            # only tests with "cancel" in the name
```

Expected result: all tests pass, plus 2 `xfailed` (the known web bugs above).

**Android tests** need a running emulator and Appium server:

```bash
npm install -g appium
appium driver install uiautomator2@8.7.3       # driver version matching Appium 3.x
appium                                         # start the server (leave it running)
pytest tests/mobile -v                         # in a second terminal, with the emulator running
```

The My Demo App `.apk` comes from the [Sauce Labs releases page](https://github.com/saucelabs/my-demo-app-android/releases). CI skips the mobile folder, since GitHub's runners have no emulator.

## What's next

- iOS automation with Appium (XCUITest)
- Testing AI / LLM features
