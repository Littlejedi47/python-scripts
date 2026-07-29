file_name = 'pi.txt'

with open(file_name, 'w') as file_object:
    file_object.write("3.1415926535\n8979323846\n2643383279")

with open(file_name, 'r') as file_object:
    for line in file_object:
        print(line.rstrip())