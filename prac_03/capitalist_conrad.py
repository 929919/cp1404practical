"""Capitalist Conrad stock price simulator with file output."""

import random

# Constants
STARTING_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
FILENAME = 'stock_price_simulation.txt'


def main():
    """Simulate stock price changes and write output to a file."""
    price = STARTING_PRICE
    number_of_days = 0

    # Open file for writing
    out_file = open(FILENAME, 'w')

    # Print starting price
    print(f"Starting price: ${price:,.2f}", file=out_file)


    # Run the simulation
    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1

        # Decide randomly whether price increases or decreases
        if random.randint(0, 1) == 0:
            price -= price * random.uniform(0, MAX_DECREASE)
        else:
            price += price * random.uniform(0, MAX_INCREASE)

        # Print day and price to file
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)


    # Close the file
    out_file.close()


main()
