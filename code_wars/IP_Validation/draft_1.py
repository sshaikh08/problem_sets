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

# word = 'Hello World'
# print(word.find('Wor'))  # Returns the starting position of the phrase you're looking for
# print(word.find('uhdsafij')) # Return -1 if the string is not found
# print(word.index('Wor'))
# print(word.index('uhdsafij')) # return a valueError

# test_string = '3s..st.st.w'
# test_string_list = test_string.split('.')
# print(test_string_list)

test_string_2 = '123.274.54.37'
test_string_list = test_string_2.split('.')
def is_valid_chars(strings_to_check):
    string_list = strings_to_check.split('.')

    empty = []

    if string_list is empty:
        return False
    else:
        pass
    print(string_list)
    first_char = int(string_list[0][0])
    max_octet_value = 256
    #print(string_list)

    for i in range(len(string_list)):
        if first_char < 1 or int(string_list[i]) > max_octet_value:
            return False
        else:
            return True
print(test_string_2)
is_ipAdress_valid = is_valid_chars('12.255.56.1')
print(is_ipAdress_valid)
