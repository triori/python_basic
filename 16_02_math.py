# This part of the code calculates the squaring of a number
print('(1) This program calculates the square of a number.')
number_to_sq = float(input('Input a number: '))
print('The square of your number is:')
print(number_to_sq ** 2)

# This part of the code calculates the average of three numbers
print('(2) This program calculates the average of three numbers.')
first_number_to_find_average = float(input('Input the first number: '))
second_number_to_find_average = float(input('Input the second number: '))
third_number_to_find_average = float(input('Input the third number: '))
average = (first_number_to_find_average + second_number_to_find_average + third_number_to_find_average) / 3
print('The average of your numbers is:')
print(average)

# This part of the code turns minutes into hours and minutes
print('(3) This program turns minutes into hours and minutes.')
minutes_total = int(input('Input the number of minutes: '))
hours, minutes = divmod(minutes_total, 60)
print('The number of hours is:')
print(hours)
print('The number of minutes is:')
print(minutes)

# This part of code calculates the discount from a price
print('(4) This program calculates the discount from a price.')
original_price = float(input('Input the original price: '))
discount_percentage = float(input('Input the discount percentage: '))
discount_amount = original_price * (discount_percentage / 100)
final_price = original_price - discount_amount
print('The final price after discount is:')
print(final_price)

# This part of the code calculates the last digit of a number (works only for decimal numbers)
print('(5) This program calculates the last digit of a number.')
number_to_find_last_digit = int(input('Input a number: '))
last_digit = number_to_find_last_digit % 10
print('The last digit of your number is:')
print(last_digit)

# this part of the code calculates a perimeter of a rectangle
print('(6) This program calculates the perimeter of a rectangle.')
length_of_rectangle = float(input('Input the length of the rectangle: '))
width_of_rectangle = float(input('Input the width of the rectangle: '))
perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
print('The perimeter of the rectangle is:')
print(perimeter_of_rectangle)

# This part of code prints all the digits of a number (works only for 4-digit numbers)
print('(7) This program prints all the digits of a number (works only for 4-digit numbers).')
number_to_print_digits = int(input('Input a 4-digit number: '))
thousands_digit = number_to_print_digits // 1000
hundreds_digit = (number_to_print_digits % 1000) // 100
tens_digit = (number_to_print_digits % 100) // 10
ones_digit = number_to_print_digits % 10
print('The digits of your number are:')
print(thousands_digit)
print(hundreds_digit)
print(tens_digit)
print(ones_digit)