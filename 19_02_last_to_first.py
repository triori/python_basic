# in this case I use list to iterate all the examples
examples = [[12, 3, 4, 10], [1], [], [12, 3, 4, 10, 8]]
# prepare iterator
i = 0
# prepare length of examples to avoid calculating it in each iteration
length_of_examples = len(examples)

# basic solution
# iterate through all the examples and move the last element to the first position
while i < length_of_examples:
    # get the current example
    example = examples[i]
    # print the original example with no newline to show the transformation
    print(example, '=>', end=' ')
    # check if the example is not empty to avoid errors
    if len(example) > 0:
        # remove the last element and insert it at the beginning of the list
        last_element = example.pop()
        example.insert(0, last_element)
    # the operation could be the same for empty and non-empty lists, so we can print the example in both cases
    print(example)
    i += 1
print('---\n')

# more elegant solution
i = 0
# iterate through all the examples and move the last element to the first position
while i < length_of_examples:
    # get the current example
    example = examples[i]
    # print the original example with no newline to show the transformation
    print(example, '=>', end=' ')
    # false if the list is empty so we can skip replacement step
    if example:
        example.insert(0, example.pop())
    print(example)
    i += 1