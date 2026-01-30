import json


filename = 'username.json'
try:
    with open(filename, 'a+', encoding='utf-8') as f:
        get_username = input('Enter your username: ')
        
except FileNotFoundError:
    username = input('Enter username: ')
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(username, f)
        print(f"We'll remember you the next time you come back, {username}!")
else:
    print(f'welcome back, {get_username}!')