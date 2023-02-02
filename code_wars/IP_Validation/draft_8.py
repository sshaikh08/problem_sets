from codewars_test import assert_equals
from string import digits
from itertools import chain


def is_valid_IP(string_to_check):
    if string_to_check == '':
        return False
    string_list = string_to_check.split('.')
    print(string_list)
    print(list(digits))

    chars_in_string_list = list(chain(*string_list))
    print(chars_in_string_list)
    is_char_int_list = [x is True if x in list(digits) else x is False for x in chars_in_string_list]
    print(is_char_int_list)

    max_octet_value = 256
    first_chars = [i[0] for i in string_list]
    if all(is_char_int_list):
        valid = True
        for i in range(len(string_list)):
            if len(string_list[i]) == 0 or int(string_list[i]) > max_octet_value or (
                    len(string_list[i]) > 1 and int(string_list[i][0]) == 0):
                valid = False
                break
        return valid