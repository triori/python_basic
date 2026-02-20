# in this case I use list to iterate all the examples
examples = [[1, 2, 3, 4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5], [1], []]
# prepare iterator
i = 0
# prepare length of examples to avoid calculating it in each iteration
length_of_examples = len(examples)

# basic solution
# iterate through all the examples and separate the list by the rules from the task
while i < length_of_examples:
    # get the current example
    example = examples[i]
    # print the original example with no newline to show the transformation
    print(example, '=>', end=' ')
    # prepare two empty lists to store the first and second parts of the original list
    first_list, second_list = [], []
    # by the rule if the list is empty, we should print two empty lists, so we can check it at the beginning of the iteration to avoid errors
    if len(example) == 0:
        print([first_list, second_list])
    # if the list is not empty, we should check if it has an even or odd number of elements to separate it correctly
    elif len(example) % 2 == 0:
        first_list = example[:len(example) // 2]
        second_list = example[len(example) // 2:]
        print([first_list, second_list])
    # if the list has an odd number of elements, we should include the middle element in the first list, so we can calculate the index of the middle element and separate the list accordingly
    else:
        first_list = example[:len(example) // 2 + 1]
        second_list = example[len(example) // 2 + 1:]
        print([first_list, second_list])
    i += 1
print('---\n')

# more elegant solution
i = 0
# iterate through all the examples and separate the list by the rules from the task
while i < length_of_examples:
    # get the current example
    example = examples[i]
    # print the original example with no newline to show the transformation
    print(example, '=>', end=' ')
    # it can works even with empty list
    middle_index = (len(example) + 1) // 2
    # separate the list by middle point
    first_list = example[:middle_index]
    second_list = example[middle_index:]
    print([first_list, second_list])
    i += 1