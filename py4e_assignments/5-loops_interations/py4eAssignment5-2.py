# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line
# below. Convert the extracted value to a floating point number and print it out.

# My Solution:

# largest = None
# smallest = None
# number_list = []
#
#
# while True:
#     try:
#         num = input('Enter a number: ')
#         if num == 'done':
#             break
#         else:
#             number_list.append(int(num))
#     except ValueError:
#         print('Invalid input')
#
#
# largest = max(number_list)
# smallest = min(number_list)
#
# print(f'Maximum is {largest}')
# print(f'Minimum is {smallest}')

#############################################

# ChatGPT Solution:

number_list = []
num = input('Enter a number (or "done" to exit): ')

while num != 'done':
    try:
        number = int(num)
        number_list.append(number)
    except ValueError:
        print('Invalid input. Please enter a number.')

    num = input('Enter a number (or "done" to exit): ')

if number_list:
    largest = max(number_list)
    smallest = min(number_list)
    print(f'Maximum is {largest}')
    print(f'Minimum is {smallest}')
else:
    print('No numbers entered.')




