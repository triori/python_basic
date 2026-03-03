print("Welcome to the multiplication digits program!")
customers_number = int(input("Input a number: "))
# to avoid the mutation of the original number, we will work with a copy of it
number = customers_number
# the main loop continues until the number has only one digit
while number >= 10:
    temporary_multiplication_result = 1
    for digit in str(number):
        temporary_multiplication_result *= int(digit)
    number = temporary_multiplication_result

print(f"Result: {customers_number} -> {number}")