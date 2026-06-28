"""Test project — algorithm tasks 1.1-1.3 plus bracket-sequence analysis.

Run with:  python3 main.py

The program shows an interactive menu and lets the user enter values from
the console for every task. All numeric input is validated, so invalid
input shows a friendly message instead of crashing.
"""


def check_number():
    """Task 1.1: if the entered number is greater than 7, print 'Hello'.

    Accepts floats as well as integers, and prints a clear message when the
    number is 7 or smaller.
    """
    try:
        num = float(input("Enter a number: "))
    except ValueError:
        print("That is not a valid number.")
        return

    if num > 7:
        print("Hello")
    else:
        print(f"{num:g} is not greater than 7.")


def check_name():
    """Task 1.2: greet the name 'John', otherwise report it is unknown.

    Matching is case-insensitive and ignores surrounding spaces, so 'JOHN',
    ' john ' and 'John' are all accepted.
    """
    name = input("Enter a name: ").strip()
    if name.lower() == "john":
        print("Hello, John")
    else:
        print("There is no such name")


def filter_multiples_of_3():
    """Task 1.3: print the array elements that are multiples of 3.

    Reads numbers separated by spaces. Integer and float values are both
    supported (e.g. 9 and 9.0 are multiples of 3).
    """
    raw = input("Enter the array elements separated by spaces: ").split()
    try:
        numbers = [float(x) for x in raw]
    except ValueError:
        print("All elements must be numbers.")
        return

    if not numbers:
        print("No numbers were entered.")
        return

    # Keep integer-looking values as ints so output reads cleanly (9 not 9.0).
    multiples = [int(n) if n.is_integer() else n for n in numbers if n % 3 == 0]

    if multiples:
        print("Multiples of 3:", multiples)
    else:
        print("No multiples of 3")


def analyze_brackets():
    """Bracket task: check whether a bracket sequence is valid.

    Validity rules: every opening bracket must be closed by the matching
    closing bracket, in the correct order. Reports the first error position
    and, for the assignment sequence, suggests a correction.
    """
    default = "[((())()(())]]"
    seq = input(f"Enter a bracket sequence (Enter for '{default}'): ").strip()
    if not seq:
        seq = default

    valid, reason = is_valid_sequence(seq)
    print(f"Sequence: {seq}")
    if valid:
        print("Result: VALID")
    else:
        print(f"Result: INVALID — {reason}")
        print(f"  '(' opened {seq.count('(')}, closed {seq.count(')')}")
        print(f"  '[' opened {seq.count('[')}, closed {seq.count(']')}")
        if seq == default:
            print("Suggested correction: [((())()(()))]  "
                  "(add one ')' and remove one ']')")


def is_valid_sequence(seq):
    """Return (is_valid, reason). Validates () and [] nesting with a stack."""
    closers = {")": "(", "]": "["}
    stack = []
    for index, char in enumerate(seq):
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack:
                return False, f"'{char}' at position {index} closes nothing"
            if stack[-1] != closers[char]:
                return False, (f"'{char}' at position {index} does not match "
                               f"'{stack[-1]}'")
            stack.pop()
    if stack:
        return False, f"{len(stack)} bracket(s) left open: {''.join(stack)}"
    return True, "balanced"


def main():
    """Show the menu and dispatch the chosen task until the user exits."""
    menu = (
        "\n--- Menu ---\n"
        "1. Check number > 7\n"
        "2. Check name\n"
        "3. Filter multiples of 3\n"
        "4. Check bracket sequence\n"
        "5. Exit"
    )
    actions = {
        "1": check_number,
        "2": check_name,
        "3": filter_multiples_of_3,
        "4": analyze_brackets,
    }

    while True:
        print(menu)
        try:
            choice = input("Choose (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye, thanks!")
            break

        if choice == "5":
            print("Bye, thanks!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Wrong option")


if __name__ == "__main__":
    main()
