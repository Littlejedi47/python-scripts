import json
import secrets
import string

def password_generation(length=12):
    user_input = input("Length of the password(default is 12): ")
    if user_input == "":
        length = 12
    else:
        try:
            length = int(user_input)
        except ValueError:
            print("Invalid input, Using default length of 12.")
            length = 12
    alphabet = string.ascii_letters + string.digits
    generated_password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return generated_password

        
def list_passwords():
        with open(filename) as view_file:
            vault = json.load(view_file)

            for entry in vault:
                for service, details in entry.items():
                    print("")
                    print(f"Service: {service}")
                    print(f"Website: {details['website']}")
                    print(f"Username: {details['username']}")
                    print(f"Password: {details['password']}")
                    print("\n================================================\n")


greeter = int(input("""========================
 Python Password Vault
========================

1. Add password
2. View passwords
3. Search
4. Delete
5. Generate password
6. Exit

Choice: """))

filename = "vault.json"

if greeter == 1:
    with open(filename, 'r+') as write_file:
        try:
            vault = json.load(write_file)
        except (FileNotFoundError, json.JSONDecodeError):
            vault = {}

        service = input("\nService(Required!): ")
        while service == "":
            service = input("\nService(Required!): ")
                
        website = input("\nWebsite: ")
        username = input("\nUsername: ")
        password = input("\nPassword: ")
        vault[service] = {
            f"{service}" : {
                "website": website,
                "username": username,
                "password": password
            }
        }
        write_file.seek(0)
        write_file.truncate()
        json.dump(vault, write_file, indent=2)

elif greeter == 2:
    list_passwords()

elif greeter == 3:
    with open(filename) as search_file:
        vault = json.load(search_file)
        search_service = input("\nService name: ")

        found = False
        for entry in vault:
            for service, details in entry.items():
                if service == search_service:
                    found = True
                    print("\nFound:")
                    print("")
                    print(f"Service: {service}")
                    print(f"Website: {details['website']}")
                    print(f"Username: {details['username']}")
                    print(f"Password: {details['password']}")
                    print("\n================================================\n")

        if not found:
            print("Service not found!")

elif greeter == 4:
    # Read the vault
    with open(filename, 'r') as file:
        vault = json.load(file)
    
    # Show current passwords (optional)
    list_passwords()
    
    # Get service to delete
    service_to_remove = input("\nWhich one do you want to delete? ")
    
    # Find and remove the service
    removed_item = None
    for index, item in enumerate(vault):
        if service_to_remove in item:
            removed_item = vault.pop(index)
            break
    
    # Write back to file
    with open(filename, 'w') as file:
        json.dump(vault, file, indent=2)
    
    # Show result
    if removed_item:
        print(f"Removed: {removed_item}")
    else:
        print(f"Service '{service_to_remove}' not found!")

elif greeter == 5:
    print(f"Your generated password is: {password_generation()}")