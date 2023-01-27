import random
import string

acceptable_characters = string.ascii_lowercase + string.digits
test_length = random.randrange(1, 13)
random_string_location = random.randrange(0, test_length)

test_string = ''.join(random.choice(acceptable_characters) for _ in range(test_length))

print('test_string before: ' + test_string)

for _ in range(test_length):
    test_string = test_string[:random.randrange(0, test_length)] \
                  + '.' \
                  + test_string[random.randrange(0, test_length):]

print('test_length: ' + str(test_length))
print('random_string_location: ' + str(random_string_location))
print('test_string after: ' + test_string)
print('number of periods in test_string: ' + str(test_string.count('.')))
