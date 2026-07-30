import json
import secrets
import string

def display_options(): 
    print("""========================
 Python Password Vault
========================

1. Add password
2. View passwords
3. Search
4. Delete
5. Generate password
6. Exit""")


def password_generator(length=12):
    user_input = input("Length of the password (default is 12): ")
    
    # Handle empty input or "default" keyword
    if user_input == "" or user_input.lower() == "default":
        length = 12
    else:
        try:
            # Convert to integer
            length = int(user_input)
            
            # Now check if it's in valid range
            if not (12 <= length <= 99):
                print("Invalid input (must be 12-99). Using default length of 12.")
                length = 12
                
        except ValueError:
            print("Invalid input. Using default length of 12.")
            length = 12
    
    # Generate password
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    generated_password = ''.join(secrets.choice(alphabet) for _ in range(length))
    print(generated_password)
    return generated_password
        

while True:
    display_options()
    
    try:
        try:
            with open("vault.json", '+a') as write_file:
                vault = json.load(write_file)
                vault = {}
        except (FileNotFoundError, json.JSONDecodeError):
            with open("vault.json", 'w') as write_file:
                vault = json.load(write_file)
                vault = {}

        chosen_option = int(input("\n\nchoice: "))
        while chosen_option in range(1,7):
            continue
        else:
            print("Invalid, Input must be a number(1-6)!")
            chosen_option = int(input("\n\nchoice: "))
    except ValueError:
        print("Invalid, Input must be a number(1-6)!")
        chosen_option = int(input("\n\nchoice: "))

    #  Add password

    if chosen_option == 1: 
        service = input(f"Name of service(Required!): ")
        website = input(f"Website address: ")
        username = input(f"Username: ")
        password = input(f"Password: ")

        vault[service] = {
            "Website": website,
            "Username": username,
            "Password": password
        }
        write_file.seek(0)
        write_file.truncate()
        json.dump(vault, write_file, indent=2)
        print("Password saved successfully!")









        
    elif chosen_option == 6:
        print("Closing Password Manager...")
        exit