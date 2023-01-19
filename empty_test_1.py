import random
import string

acceptable_characters = string.ascii_lowercase + string.digits
test_length: int = random.randrange(19) + 1
# test_length = 6
random_string_location = random.randrange(0, test_length)


test_string = ''.join(random.choice(acceptable_characters) for _ in range(test_length))

print('test_string before: ' + test_string)

for _ in range(4):
    test_string = test_string[:random.randrange(0, test_length+1)] \
                  + '.' \
                  + test_string[random.randrange(0, test_length+1):]

print('test_length: ' + str(test_length))
print('random_string_location: ' + str(random_string_location))
print('test_string after: ' + test_string)
