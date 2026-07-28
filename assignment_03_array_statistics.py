# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calc_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calc_average(numbers):
    return calc_sum(numbers) / len(numbers)


def calc_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def calc_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def main():
    try:
        n = int(input("How many numbers? "))
        
        if n <= 0:
            print("Error: Number of elements must be greater than 0.")
            return

        numbers = []
        for i in range(1, n + 1):
            val = float(input(f"Enter number {i}: "))
            numbers.append(val)

        print("\nResults:")
        # If numbers are integers, format output as integers; otherwise display normally
        sum_val = calc_sum(numbers)
        max_val = calc_max(numbers)
        min_val = calc_min(numbers)
        
        print(f"Sum:     {int(sum_val) if sum_val.is_integer() else sum_val}")
        print(f"Average: {calc_average(numbers)}")
        print(f"Maximum: {int(max_val) if max_val.is_integer() else max_val}")
        print(f"Minimum: {int(min_val) if min_val.is_integer() else min_val}")

    except ValueError:
        print("Error: Please enter valid numerical values.")


if __name__ == "__main__":
    main()