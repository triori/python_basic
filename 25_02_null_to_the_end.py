example = [0, 1, 0, 12, 3]
# example = [0]
# example = [1, 0, 13, 0, 0, 0, 5]
# example = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

i = len(example) - 1
print(example, '=>', end=' ')
# false if the list is empty so we can skip replacement step
if example:
    # we need to iterate from the end to the beginning to avoid skipping elements after replacement
    while i >= 0:
        if example[i] == 0:
            example.append(example.pop(i))
        i -= 1
# that could be work even with empty list, but we check it at the beginning to avoid errors
print(example)