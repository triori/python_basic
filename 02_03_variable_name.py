import keyword
import string

potential_variable_name = input("Enter a potential variable name: ")
is_valid_variable_name = True
unacceptable_characters = string.punctuation.replace("_", "") + string.whitespace

if not potential_variable_name:
    # empty string is not a valid variable name
    is_valid_variable_name = False
elif potential_variable_name[0].isdigit():
    # variable name cannot start with a digit
    is_valid_variable_name = False
elif any(char.isupper() for char in potential_variable_name):
    # variable name cannot contain uppercase letters
    is_valid_variable_name = False
elif any(char in unacceptable_characters for char in potential_variable_name):
    # variable name cannot contain special characters or spaces (except for _)
    is_valid_variable_name = False
elif all(char == "_" for char in potential_variable_name) and len(potential_variable_name) > 1:
    # variable name cannot consist entirely of more than one underscore
    is_valid_variable_name = False
elif potential_variable_name in keyword.kwlist:
    # variable name cannot be a reserved keyword
    is_valid_variable_name = False

print(is_valid_variable_name)
