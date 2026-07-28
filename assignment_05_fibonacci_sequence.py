# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci(n):
    """Generates and prints the first N terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return

    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(map(str, sequence)))


def is_fibonacci(num):
    """Checks whether a given non-negative integer is a Fibonacci number."""
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num


def main():
    try:
        # Part A
        n = int(input("How many terms? "))
        generate_fibonacci(n)

        print()  # Blank line for spacing

        # Part B
        check_num = int(input("Enter a number to check: "))
        if is_fibonacci(check_num):
            print(f"{check_num} is a Fibonacci number.")
        else:
            print(f"{check_num} is NOT a Fibonacci number.")

    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()
