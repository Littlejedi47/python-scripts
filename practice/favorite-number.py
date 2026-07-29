import json

def get_fav_num():
    fav_num = input('What is your favorite number? ')
    filename = 'favorite-number.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
        print('I will remember this!')

def read_fav_num():
    filename = 'favorite-number.json'
    with open(filename, 'r') as f:
        fav_num = json.load(f)
        print('I will remember this!')


def check_fav_num():
    try:
        filename = 'favorite-number.json'
        with open(filename) as f_obj:
            load_num = json.load(f_obj)
            if load_num == "":
                get_fav_num()
            else:
                print(f'your favorite number is {load_num}')
    except FileNotFoundError:
        get_fav_num()

try:
    filename2 = 'favorite-number.json'
    with open(filename2, 'w'):
        load_number = json.load(filename2)
        if load_num == "":
            getnum = input("What si your favorite number: ")
            json.dump(getnum, filename2)
            print('I will remember this!')
        else:
            print(f"I know your favorite number! It's {load_number}!")
except FileNotFoundError:
    pass