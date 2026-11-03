# Lesson 4 notes - pytest

## Big ideas
1. **Function** (`def name():`) = a named block of steps.
2. pytest runs every function whose name starts with `test_`, in files named `test_*.py`.
   Anything else is **silently skipped** - no error, no warning.
3. `(page: Page)` = a **fixture**: pytest opens a fresh browser tab before the test and closes it after.
   No more `with` / `launch` / `close`.
4. Each test is **independent**: fresh browser, own login. One failure does NOT stop the others.
   You see ALL problems in one run.

## Commands
```bash
pip install pytest-playwright                       # one time only
pytest lessons/lesson-04 -v                          # run, invisible browser (fast)
pytest lessons/lesson-04 -v --headed --slowmo 500   # watch it
```
- `-v` = list each test with PASSED / FAILED
- `command not found` = typo, OR the tool isn't installed

## Experiments I did
- Broke one test -> `1 failed, 2 passed`. The others still ran.
- Renamed `test_login_works` -> `check_login_works` -> pytest found only 2 tests.
  Danger: a misnamed test never runs, and nobody notices.
