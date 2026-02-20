example = [1, 2, 3, 4, 5, 6]
# example = [1, 2, 3]
# example = [1, 2, 3, 4, 5]
# example = [1]
# example = []

print(example, '=>', end=' ')
# false if the list is empty so we can skip replacement step
if example:
    example.insert(0, example.pop())
# that could be work even with empty list, but we check it at the beginning to avoid errors
print(example)
