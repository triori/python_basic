agree_to_continue = True

while agree_to_continue:
    first_value = float(input('Input the first value: '))
    operation = input('Input the operation (+, -, *, /): ')
    second_value = float(input('Input the second value: '))

    print('Our expression looks like this:', first_value, operation, second_value)

    # check that operation is valid
    if operation not in ['+', '-', '*', '/']:
        # print user friendly errormessage and no calculation
        print('Invalid operation. Please choose one of the following: +, -, *, /')
    else:
        if operation == '+':
            result = first_value + second_value
        elif operation == '-':
            result = first_value - second_value
        elif operation == '*':
            result = first_value * second_value
        elif operation == '/':
            if second_value != 0:
                result = first_value / second_value
            else:
                print('Error: Division by zero is not allowed.')
                result = 'Error'

        if result != 'Error':
            print('The result of the operation is:', result)

        agree_to_continue = input('Do you want to perform another calculation? (y/n): ')
        if agree_to_continue == 'n':
            agree_to_continue = False
        elif agree_to_continue != 'y' and agree_to_continue != 'n':
            print('Invalid input. Exiting the program.')
            agree_to_continue = False