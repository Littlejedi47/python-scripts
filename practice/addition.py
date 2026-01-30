while True:
    try:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the seconed number: '))
    
    except KeyboardInterrupt:
        print('\n\n\nTask ended!\n\n')
    
    except ValueError:
        print('Please add a number!')
    else:
        print(f'{num1} + {num2} = {num1 + num2}')