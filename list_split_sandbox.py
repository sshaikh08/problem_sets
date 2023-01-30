import string

list_1 = ['12', '255', '56', '1']

list_1_split = [x.split() for x in list_1]

print('list_1_split: ')
print(list_1_split)

string_1 = string.ascii_letters
string_2 = '123.456.789.0'
string_2_list = string_2.split('.')

print('The alphabet: ' + string_1)
print(string_1.split())
print(list(string_1))
print(string_2_list)

chars_in_string_list = [list(x) for x in string_2_list]
print(chars_in_string_list)
