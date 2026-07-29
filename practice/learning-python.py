
filename = "learning-python.txt"

with open(filename, 'r') as file:
    text = file.read()

replaced = text.replace('i can', 'you can')
print(replaced)