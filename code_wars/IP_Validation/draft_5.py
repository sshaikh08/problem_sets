import string

def is_valid_IP(strings_to_check):
    print('Strings to Check')
    print(strings_to_check)

    string_list = strings_to_check.split('.')
    print('string_list before:')
    print(string_list)

    is_only_int_list = [x is True if x in string.digits else x is False for x in string_list]

    print('is_only_int_list:')
    print(is_only_int_list)

    first_char = None

    if all(is_only_int_list) is False:
        string_list = ['0']

    # print(type(empty))
    # if string_list is empty:
    #     return False
    # else:
    #     pass
    print(strings_to_check)
    print(string_list)



    first_chars = [i[0] for i in string_list ]
    print('First Chars: ')
    print(first_chars)

        # int(string_list[0][0])


    max_octet_value = 256
    # print(string_list)

    for i in range(len(string_list)):
        if (len(string_list[i]) > 1 and int(first_chars[i]) < 1) or int(string_list[i]) > max_octet_value:
            return False
        else:
            return True

test_string_2 = ''
# test_string_2 = 'abc.def.ghi.jkl'
print(type(test_string_2))
test_string_list = test_string_2.split('.')

print(test_string_2)
is_ipAddress_valid = is_valid_IP(test_string_2)
print('Is the IP Address valid?\n' + str(is_ipAddress_valid))