# Lesson 1 notes

## Big ideas
1. Every test = **do some steps -> check what happened**.
2. `assert` is the check. No assert = no test, just a script.
3. **A test only catches what you check.** With a wrong password, lines 7-8 still
   "work" (they type and click). Only the `assert` notices the login failed.

## Words
- **Python** - the language you write instructions in.
- **Playwright** - the robot that controls the browser (made by Microsoft).
- **Chromium** - the browser Playwright drives (Chrome is built on it).
- **Terminal** - type commands to your Mac.
- **pip** - app store for Python tools (`pip install playwright`).
- **venv** - a separate box for this project's tools. `(venv)` = box is on.
- **Headless** - browser runs with no visible window.
- **Selector** (`#user-name`) - the address of one element on the page.

## How to run
```bash
cd ~/qa-practice
source venv/bin/activate
python3 lessons/lesson-01/test_login.py
```
No output = PASSED. An `AssertionError` = FAILED.

## Try it (break it on purpose)
Change `secret_sauce` to `wrong_password`, predict what happens, then run it.
Change it back when done.
