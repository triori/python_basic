example = [0, 1, 7, 2, 4, 8]
# example = [1, 3, 5]
# example = [6]
# example = []

final_value = 0
i = 0
example_length = len(example)
example_last_index = example_length - 1

# sum elements at even indices (0, 2, 4, ...)
while i < example_length:
    if i % 2 == 0:
        final_value += example[i]
    i += 1

# multiply by the last element (skip if list is empty)
if example:
    final_value = final_value * example[example_last_index]

print(final_value)