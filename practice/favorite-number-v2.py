import json

def get_username():
    username = input("What is your username? ")
    filename = "users.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    print("I'll remember you the next time you come back!")

def greet_user():
    filename = "users.json"
    with open(filename, 'r') as f:
        username = json.load(f)
    print(f"Welcome back, {username}!")

def check_username():
    filename = "users.json"
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        get_username()
    else:
        greet_user()

check_username()
