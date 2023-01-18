# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
# they consist of four octets, with values between 0 and 255, inclusive.

import random
import string

acceptable_characters = string.ascii_lowercase + string.digits
test_length = random.randrange(20)
test_string = ''.join(random.choice(acceptable_characters) for _ in range(test_length))

print(f'test_length: {test_length}')
print(f'test: {test_string}')
print(acceptable_characters)


def is_valid_IP(input_str):
    return input_str.count('.')


ip_wrong_test_example = ''

test_2 = is_valid_IP('pass')
