"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
"""Get a valid integer from the user without crashing."""

def main():
    """Prompt the user until a valid integer is entered."""
    is_finished = False
    result = None

    while not is_finished:
        try:
            result = int(input("Enter a valid integer: "))
            is_finished = True  # Exit loop when input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("Valid result is:", result)


main()
