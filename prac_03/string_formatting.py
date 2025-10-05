"""String formatting using f-strings."""

def main():
    """Display formatted strings with alignment examples."""
    guitar_name = "Gibson L-5 CES"
    year = 1922
    guitar_cost = 16036

    # Using f-string formatting to produce the required output
    print(f"{year} {guitar_name} for about ${guitar_cost:,}!")

    # Using a for loop with f-string formatting to generate the required output
    for exponent in range(11):
        power_of_two = 2 ** exponent
        print(f"2 ^ {exponent:2} is {power_of_two:4}")


main()
