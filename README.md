# QA Automation Practice

![Tests](https://github.com/EJ-qatest/qa-practice/actions/workflows/tests.yml/badge.svg)

## About me

I'm a QA engineer with 6 years of manual testing experience across web, iOS, and Android apps, plus some hardware testing.
I'm now building my automation skills, and this repo is where I practice: turning the test cases I'd normally run by hand
into reliable, automated tests that run on every code change.

## What's in this repo

| Folder | What it shows |
|--------|---------------|
| `lessons/lesson-09` | UI tests for an e-commerce site using the **Page Object Model** (login, cart, checkout, sorting, logout) |
| `lessons/lesson-10` | **API tests** covering create, read, update, delete, plus negative cases (404) |
| `lessons/lesson-08` | Shared setup with **pytest fixtures** and `conftest.py` |
| `practice/` | Solo practice: API data checks, debugging exercises |
| `.github/workflows/` | **CI**: every push runs the test suite automatically on GitHub Actions |

## Tech stack

Python · Playwright · pytest · requests · Git · GitHub Actions

## My test strategy

- **Unhappy paths matter as much as happy ones.** Alongside "login works", I test what should *fail*: a locked-out user, a missing password, a request for a user that doesn't exist (404).
- **Check the middle, not just the end.** In the checkout test I confirm the cart badge and the cart contents before checking out, so a failure points straight to the step that broke.
- **Checks should be strict where it matters and flexible where it doesn't.** I match exact text for prices and headings, but use "contains" for messages whose wording may change, so tests don't break for harmless reasons.
- **Wait for the right thing, never for a fixed time.** Tests wait for the new page's content to appear instead of using sleeps, which keeps them fast and avoids flaky failures.
- **Every test is independent.** Each one starts with a fresh browser and its own login, so one failure never hides or causes another.

## How to run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest lessons/lesson-09 lessons/lesson-10 practice -v
```

## What's next

- Mobile automation with Appium (Android + iOS)
- Testing AI / LLM features
