# Issues Found and Fixed - radio_schedule.py

Baseline: Pylint 2.41/10, Bandit 3 issues (1 Low, 2 Medium), Flake8 4 issues.
After fixes: Pylint 10.00/10, Bandit 0 issues, Flake8 0 issues. Program output is unchanged.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Use of `eval()` on a string (B307 / W0123) | Security (Medium, High confidence) | 19-23 | `overlapFree(formula)` runs `eval()` on caller-supplied text, allowing arbitrary code execution. | Removed `eval`. New `overlap_free(first_end_hour, second_start_hour)` takes plain values and returns `first_end_hour <= second_start_hour`. |
| SQL injection via string formatting (B608) | Security (Medium) | 11 | `INSERT` built with `%` formatting, so a show name like `x'); DROP TABLE slots;--` alters the query. | Parameterised query: `VALUES (?, ?, ?, ?)` with a tuple of values. |
| Hardcoded password (B105) | Security (Low) | 5 | `STUDIO_PASSWORD = "onair2024"` is committed in source. | Read from environment: `os.environ.get("STUDIO_PASSWORD", "")`. |
| Broad `except Exception` (W0718) | Bug / Code smell | 22-23 | Swallowed every error and returned `False`, hiding real bugs (a typo looked like "slots overlap"). | Removed with the `eval` redesign; the function is now a pure comparison with no try/except. |
| Global state out of sync (W0603, C0103) | Bug / Design | 6, 10, 12, 27, 31 | Global `booked_minutes` was updated by `addSlot` but never reduced by `removeSlot`, so it went stale. `morningShows` also relied on it as a guard. | Removed the global; `morning_shows` queries the database directly, which is the single source of truth. |
| Multiple statements on one line (E701 / C0321) | Style | 27 | `if ...: return ...` on one line. | Removed the redundant guard; the function is a single clear query and list comprehension. |
| Lines too long (E501 / C0301) | Style | 4, 11, 27 | Lines of 118, 135 and 110 chars exceed 79/100. | Split SQL strings and arguments across lines. |
| Non snake_case names (C0103) | Style | 6, 9, 15, 19, 26, 31 | `addSlot`, `slotLabel`, `overlapFree`, `morningShows`, `removeSlot`, `booked_minutes`. | Renamed to `add_slot`, `slot_label`, `overlap_free`, `morning_shows`, `remove_slot`. |
| Missing docstrings (C0114, C0116) | Style | 1, 9, 15, 19, 26, 31, 35 | No module or function docstrings. | Added a docstring to the module and every function. |
| `str.format` / `%` instead of f-strings (C0209) | Style | 11, 16 | Old-style string formatting. | `f"{show} hosted by {host}"`. |
| `main()` runs on import | Code smell | 41 | Demo ran whenever the module was imported. | Added `if __name__ == "__main__":` guard. |

## Verification

| Tool | Before | After |
|---|---|---|
| Pylint | 2.41/10 (22 messages) | 10.00/10 |
| Bandit | 3 issues (Low 1, Medium 2, High 0) | No issues identified |
| Flake8 | 4 issues (E501 x3, E701 x1) | 0 issues |

Program output, before and after (identical):

```
Sunrise Beats hosted by Vik
True ['Sunrise Beats']
```
