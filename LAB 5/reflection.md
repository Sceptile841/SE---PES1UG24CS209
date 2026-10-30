# Reflection - Lab 5: Static Code Analysis

**1. Which tool was most useful, and which findings were easiest or hardest to fix?**
Bandit was the most valuable because its three findings (`eval`, SQL string formatting, hardcoded password) were real security risks that I would not have spotted by just running the program, which "worked". Flake8 findings were the easiest (splitting lines). The hardest was `eval`, because it needed a small redesign (`overlap_free` now takes values instead of a formula string) rather than a one-line patch.

**2. Were there false positives or findings you disagreed with?**
The hardcoded password warning (B105) is only Low severity and the value was never actually used, so it looked minor, but it is still a bad habit that leaks secrets via source control, so I fixed it. Pylint's naming and docstring messages are style rules rather than bugs; they matter for consistency but do not change behaviour.

**3. How would you use static analysis in a real workflow?**
Run all three tools automatically on every commit or pull request (a pre-commit hook plus a CI job) and fail the build on any Bandit finding, any Flake8 error, or a Pylint score under 9.5. That catches problems while they are cheap to fix, before review.

**4. How did static analysis improve this code?**
Pylint went from 2.41 to 10.00, Bandit from 3 issues to 0, and Flake8 from 4 to 0. Beyond the numbers, the code is safer (no code execution or SQL injection), more correct (the stale `booked_minutes` global is gone, so the database is the single source of truth), and easier to read and test (snake_case names, docstrings, no import side effects). The tools also pointed out a real bug I would have missed: removing a slot never reduced the booked minutes.
