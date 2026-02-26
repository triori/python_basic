import random
# its not a part of task but i imagine that from -10 to 10 is a good range of random numbers
example = []
example_length = random.randint(3, 10)
for i in range(example_length):
    example.append(random.randint(-10, 10))

print(example, '=>', end=' ')
result = [example[0], example[2], example[-2]]
print(result)