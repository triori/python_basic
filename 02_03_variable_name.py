import keyword
import string

potential_variable_name = input("Enter a potential variable name: ")
is_valid_variable_name = True

if not potential_variable_name:
    # empty string is not a valid variable name
    is_valid_variable_name = False
elif potential_variable_name[0].isdigit():
    # variable name cannot start with a digit
    is_valid_variable_name = False
elif any(char.isupper() for char in potential_variable_name):
    # variable name cannot contain uppercase letters
    is_valid_variable_name = False
elif any(char in string.punctuation.replace("_", "") or char.isspace() for char in potential_variable_name):
    # variable name cannot contain special characters or spaces (except for _)
    is_valid_variable_name = False
elif any(a == "_" and b == "_" for a, b in zip(potential_variable_name, potential_variable_name[1:])):
    # variable name cannot contain consecutive underscores (I made this rule up to match the examples provided)
    is_valid_variable_name = False
elif potential_variable_name in keyword.kwlist:
    # variable name cannot be a reserved keyword
    is_valid_variable_name = False

print(is_valid_variable_name)
