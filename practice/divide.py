
while True:
    use = input('Do you want to use the calculator?(y/n)')
    if use.lower != 'n':
        try:
            first_number = int(input('First number: '))
        except ValueError:
            print('The value must an integer!')
            continue
        try:
            second_number = int(input('Second number: '))
        except ValueError:
            print('The value must an integer!')
            continue
        try:
            answer = float((first_number / second_number))
        except ZeroDivisionError:
            print("you can't divide by zero!")
        except KeyboardInterrupt:
            print('Enter a number! keyboard interrupt')
        except ValueError:
            print('Enter a number! value error')
        except TypeError:
            print('Enter a number! type error')
        else:
            print(f'{first_number} / {second_number} = {answer}')

    else:
        break