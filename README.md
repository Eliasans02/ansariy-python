# ansariy-python — Test Project

Algorithm tasks and a bracket-sequence analyzer, written in Python with
interactive console input.

## Requirements

- Python 3.6 or newer (no external libraries needed)

## How to run

```bash
python3 main.py
```

A menu appears; type a number (1–5) and press Enter to choose a task.

## Tasks

| Option | Task |
|--------|------|
| 1 | **Number > 7** — enter a number; prints `Hello` if it is greater than 7, otherwise reports it is not. Accepts integers and floats. |
| 2 | **Check name** — enter a name; prints `Hello, John` for "John" (case-insensitive), otherwise `There is no such name`. |
| 3 | **Multiples of 3** — enter numbers separated by spaces; prints the elements that are multiples of 3. Accepts integers and floats. |
| 4 | **Bracket sequence** — enter a bracket sequence (or press Enter to use the assignment's `[((())()(())]]`); reports whether it is valid and, if not, why and how to fix it. |
| 5 | **Exit** |

## Bracket task answer

The given sequence `[((())()(())]]` is **invalid**:

- Parentheses are unbalanced: 6 opening `(` vs 5 closing `)` (one `(` is never closed).
- Square brackets are unbalanced: 1 opening `[` vs 2 closing `]` (one extra `]`).
- The first error is the `]` at position 12, which tries to close while a `(` is still open.

**Corrected (valid) version:** `[((())()(()))]` — add one `)` and remove one `]`.

## Notes

- All numeric input is validated with exception handling, so invalid input
  shows a message instead of crashing.
- Task 3 uses a list comprehension to filter the multiples.
