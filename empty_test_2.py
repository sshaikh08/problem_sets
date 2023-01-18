import string
import random

# print(type(range(16)))
# print(range(16))
# print(string.ascii_letters)
# print(string.punctuation)
# print(type(random.randrange(16)))
# print(random.randrange(16))

# nums = [1, 2, 3, 4, 5]
# squared = map(lambda x: x*x, nums)
# print(list(squared))  # prints [1, 4, 9, 16, 25]

word = 'Hello World'
print(word.find('Wor'))  # Returns the starting position of the phrase you're looking for
print(word.find('uhdsafij')) # Return -1 if the string is not found
print(word.index('Wor'))
# print(word.index('uhdsafij')) # return a valueError