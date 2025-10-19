"""
Program to collect emails and automatically extract names.
"""

def extract_name(email):
    """Extract a formatted name from the email address."""
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name


def main():
    """Ask the user for emails and display extracted names."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        name = extract_name(email)
        email_to_name[email] = name
        email = input("Email: ").strip()

    print("\nStored email addresses and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
