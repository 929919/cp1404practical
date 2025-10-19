"""
Wimbledon Champions Data Processing
Estimate: 25 minutes
Actual: 20 minutes
"""

def read_wimbledon_data(filename):
    """Read Wimbledon CSV file and return data as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(',') for line in file.readlines()[1:]]


def process_wimbledon_data(data):
    """Count wins per champion and list winning countries."""
    champions = {}
    countries = set()

    for entry in data:
        champion, country = entry[2], entry[1]
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)

    return champions, sorted(countries)


def display_wimbledon_results(champions, countries):
    """Print champions and countries in the required format."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def main():
    """Run the Wimbledon data processing program."""
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champions, countries = process_wimbledon_data(data)
    display_wimbledon_results(champions, countries)


if __name__ == "__main__":
    main()
