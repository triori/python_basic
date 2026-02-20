# get first value and wrap it as float to avoid errors in case of inputting a decimal number
first_value = float(input('Input the first value: '))
# get the operation
operation = input('Input the operation (+, -, *, /): ')
# get second value the same way as first one
second_value = float(input('Input the second value: '))

# print the expression to show the user what they have inputted and what will be calculated
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