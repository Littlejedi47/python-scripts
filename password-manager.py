import json
import secrets
import string

VAULT_FILE = "vault.json"


def display_options():
    print("""========================
 Python Password Vault
========================

1. Add password
2. View passwords
3. Search
4. Delete
5. Generate password
6. Exit
""")


def load_vault():
    """Load the vault from disk."""
    try:
        with open(VAULT_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_vault(vault):
    """Save the vault to disk."""
    with open(VAULT_FILE, "w") as file:
        json.dump(vault, file, indent=2)


def password_generator():
    user_input = input("Length of the password (default is 12): ").strip()

    if user_input == "" or user_input.lower() == "default":
        length = 12
    else:
        try:
            length = int(user_input)
            if not 12 <= length <= 99:
                print("Length must be between 12 and 99. Using default (12).")
                length = 12
        except ValueError:
            print("Invalid input. Using default (12).")
            length = 12

    alphabet = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(secrets.choice(alphabet) for _ in range(length))

    print(f"\nGenerated password:\n{password}\n")
    return password


def add_password(vault):
    service = input("Service name: ").strip()

    if not service:
        print("Service name cannot be empty.")
        return

    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password (leave blank to generate): ").strip()

    if password == "":
        password = password_generator()

    vault[service] = {
        "website": website,
        "username": username,
        "password": password,
    }

    save_vault(vault)
    print("Password saved successfully!")


def view_passwords(vault):
    if not vault:
        print("Vault is empty.")
        return

    for service, info in vault.items():
        print(f"\nService : {service}")
        print(f"Website : {info['website']}")
        print(f"Username: {info['username']}")
        print(f"Password: {info['password']}")


def search_password(vault):
    service = input("Service to search: ").strip()

    if service in vault:
        info = vault[service]
        print(f"\nService : {service}")
        print(f"Website : {info['website']}")
        print(f"Username: {info['username']}")
        print(f"Password: {info['password']}")
    else:
        print("Service not found.")


def delete_password(vault):
    service = input("Service to delete: ").strip()

    if service in vault:
        del vault[service]
        save_vault(vault)
        print("Password deleted.")
    else:
        print("Service not found.")


def get_choice():
    while True:
        try:
            choice = int(input("Choice (1-6): "))

            if 1 <= choice <= 6:
                return choice

            print("Please enter a number between 1 and 6.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    vault = load_vault()

    while True:
        display_options()
        choice = get_choice()

        if choice == 1:
            add_password(vault)

        elif choice == 2:
            view_passwords(vault)

        elif choice == 3:
            search_password(vault)

        elif choice == 4:
            delete_password(vault)

        elif choice == 5:
            password_generator()

        elif choice == 6:
            print("Closing Password Manager...")
            break


if __name__ == "__main__":
    main()