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

    
def create_and_load_file():

    global vault
    try:
        with open("vault.json", '+a') as file:
            vault = json.load(file)
    except FileNotFoundError:
        with open("vault.json", 'w') as file:
            vault = json.load(file)


def password_generator(length=12):
    try:
        password_length_input = int(input("Length of password(default is 12): "))
    except ValueError:
        while password_length_input != int:
            password_length_input = int("Invalid input - please enter a number")
            while password_length_input == int and password_length_input > 12:
                length = password_length_input
            else:
                length = 12
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    generated_password = ''.join((secrets.choice(alphabet)) for _ in range(length))
    print(generated_password)
    return generated_password
        

while True:
    display_options()
    try:
        chosen_option = int(input("\n\nchoice: "))
        while chosen_option in range(1,7):
            continue
        else:
            print("Invalid, Input must be a number(1-6)!")
            chosen_option = int(input("\n\nchoice: "))
    except ValueError:
        print("Invalid, Input must be a number(1-6)!")
        chosen_option = int(input("\n\nchoice: "))

    if chosen_option == 1:
        create_and_load_file()
        service = input(f"Name of service(Required!): ")
        website = input(f"Website address: ")
        username = input(f"Username: ")
        password = input(f"Password: ")