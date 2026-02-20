example = [1, 2, 3, 4, 5, 6]
# example = [1, 2, 3]
# example = [1, 2, 3, 4, 5]
# example = [1]
# example = []

print(example, '=>', end=' ')
# it can works even with empty list
middle_index = (len(example) + 1) // 2
# separate the list by middle point
first_list = example[:middle_index]
second_list = example[middle_index:]

print([first_list, second_list])