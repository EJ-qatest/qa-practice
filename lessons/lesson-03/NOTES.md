# Lesson 3 notes - more kinds of checks

## New checks
| Check | Passes when |
|-------|-------------|
| `expect(x).to_be_visible()` | x is on screen |
| `expect(x).not_to_be_visible()` | x is gone / hidden |
| `expect(x).to_have_text("...")` | text matches EXACTLY |
| `expect(x).to_contain_text("...")` | text INCLUDES this part (safer) |

## Big ideas
1. Test that the wrong people CAN'T get in (negative tests), not just that the right ones can.
2. Check that things DISAPPEAR too - "removed but cart still says 1" is a real bug.
3. Parts of a test that depend on leftovers from earlier parts break in confusing ways.
   Make each part stand on its own (pytest helps with this in Lesson 4).

## Real bug I caught
Claude's original code assumed the password stays in the box after a failed login.
It doesn't - the site clears it. The test didn't log in. I found it by WATCHING the run,
then fixed it by filling the password again in Part B.
Lesson: **never trust code blindly, including AI code. Run it and watch it.**

## Start-of-session commands
```bash
cd ~/qa-practice
source venv/bin/activate
```
Prompt should show `(venv) ... qa-practice %`
