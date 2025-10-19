"""
Program to collect and display email addresses.
"""

def main():
    """Ask the user for email addresses and display them."""
    emails = []

    email = input("Email: ").strip()
    while email:
        emails.append(email)
        email = input("Email: ").strip()

    print("\nStored email addresses:")
    for email in emails:
        print(email)


if __name__ == "__main__":
    main()
