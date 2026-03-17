"""
Number Processing Utility

This program allows users to:
- Transform numbers (even ×2, odd ×3)
- Calculate average
- Find minimum and maximum values

Improved after applying code review practices.
"""

from typing import List


def transform_numbers(numbers: List[int]) -> List[int]:
    """
    Transforms a list of integers:
    - Even numbers are multiplied by 2
    - Odd numbers are multiplied by 3
    """
    return [(n * 2 if n % 2 == 0 else n * 3) for n in numbers]


def calculate_average(numbers: List[int]) -> float:
    """Calculates the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum(numbers) / len(numbers)


def find_min_max(numbers: List[int]) -> tuple:
    """Returns the minimum and maximum values in the list."""
    if not numbers:
        raise ValueError("List cannot be empty.")
    return min(numbers), max(numbers)


def parse_input(user_input: str) -> List[int]:
    """Converts a comma-separated string into a list of integers."""
    try:
        return [int(x.strip()) for x in user_input.split(",")]
    except ValueError:
        raise ValueError("Invalid input. Please enter only integers separated by commas.")


def display_menu():
    print("\n=== Number Processing Utility ===")
    print("1. Transform Numbers")
    print("2. Calculate Average")
    print("3. Find Min & Max")
    print("4. Exit")


def main():
    user_input = input("Enter numbers separated by commas: ")

    try:
        numbers = parse_input(user_input)
    except ValueError as e:
        print(e)
        return

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        try:
            if choice == "1":
                result = transform_numbers(numbers)
                print("Transformed Numbers:", result)

            elif choice == "2":
                avg = calculate_average(numbers)
                print("Average:", avg)

            elif choice == "3":
                minimum, maximum = find_min_max(numbers)
                print(f"Min: {minimum}, Max: {maximum}")

            elif choice == "4":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please select 1-4.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()