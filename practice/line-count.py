filename = 'lines.txt'

with open(filename, 'w') as file:
    for i in range(10):
        file.write('line\n')

with open(filename,'r')as file:
    lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")
