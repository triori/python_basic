import string

print("Welcome to the letter range printer!")
letter_range = input("Please enter a letter range (e.g. 'a-e'): ")
start_letter, end_letter = letter_range.split('-')

start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)

result_range = string.ascii_letters[start_index:end_index + 1]
print("The letters in the range are:", result_range)