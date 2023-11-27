# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is
# entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10,
# and 4 and match the output below.

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
#
# number_list = []
# num = input('Enter a number (or "done" to exit): ')
#
# while num != 'done':
#     try:
#         number = int(num)
#         number_list.append(number)
#     except ValueError:
#         print('Invalid input. Please enter a number.')
#
#     num = input('Enter a number (or "done" to exit): ')
#
# if number_list:
#     largest = max(number_list)
#     smallest = min(number_list)
#     print(f'Maximum is {largest}')
#     print(f'Minimum is {smallest}')
# else:
#     print('No numbers entered.')

# Review Solution

INVALID_INPUT_ERR_MSG = "Invalid input" # "Please enter a valid Integer"

largest = None
smallest = None

num_list = []

if __name__ == "__main__":
    while True:
        try:
            num_input = input("Enter a number: ")
            if num_input == "done":
                break
            # print(num_input)

            num_int = int(num_input)

            num_list.append(num_int)

        except ValueError as e:
            print(INVALID_INPUT_ERR_MSG)

    largest = max(num_list)
    smallest = min(num_list)

    # print(num_list)
    print(f'Maximum is {largest}\n'
          f'Minimum is {smallest}')



