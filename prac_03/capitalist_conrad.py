"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

STARTING_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175  # 17.5% increase
MAX_DECREASE = 0.05  # 5% decrease
FILENAME = 'stock_price_simulation.txt'


# Initialize variables
price = INITIAL_PRICE
print(f"${price:,.2f}")

# Open file for writing
out_file = open(FILENAME, 'w')

# Write starting price to file
print(f"Starting price: ${price:,.2f}", file=out_file)

