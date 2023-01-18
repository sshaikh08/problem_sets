import random, string

acceptable_characters = string.ascii_lowercase + string.digits
test_length = random.randrange(20)
test_length = 6
random_string_location = random.randrange(0, test_length)
string_to_be_inserted = '--------------'
test_string = None

if test_length < 1:
    test_string = 'Length of string is 0'
else:
    test_string = ''.join(random.choice(acceptable_characters) for _ in range(test_length))

print('test_string before: ' + test_string)

test_string = test_string[:random_string_location] + string_to_be_inserted + test_string[random_string_location:]

print('test_length: ' + str(test_length))
print('random_string_location: ' + str(random_string_location))
print('test_string after: ' + test_string)
