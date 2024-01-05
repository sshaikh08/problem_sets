# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the
# following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 You will parse the From line using split()
# and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print
# out a count at the end. Hint: make sure not to include the lines that start with 'From:'. Also look at the last
# line of the sample output to see how to print the count.
#
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Instructor Provided code to modify

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
#
# fh = open(fname)
# count = 0
#
# print("There were", count, "lines in the file with From as the first word")

# My Solution

file_name = input("Enter file name: ")

if len(file_name) < 1:
    file_name = "mbox-short.txt"

email_addresses = list()

with open(file_name) as file_handle:
    for line in file_handle:
        if line.startswith('From:'):
            starts_with_from = line.split()
            # print(valid_line)
            email_addresses.append(starts_with_from[1])
            # print(line)
        else:
            continue

for emai_address in email_addresses:
    print(emai_address)

count = len(email_addresses)
print(f'There were {count} lines in the file with From as the first word')

# My Solution 2 *** Will not work in automatic Grader

# Modify this by inserting 'try/except' block
# from os import path
#
# INVALID_PATH_ERR_MSG = "The file does not exist, please enter a valid path"
#
# email_addresses = list()
# file_name = ''
#
# while True:
#     try:
#         file_name = input("Enter file name: ")
#
#         if len(file_name) < 1:
#             file_name = "mbox-short.txt"
#
#         if path.isfile(file_name):
#             break
#         else:
#             raise FileNotFoundError(INVALID_PATH_ERR_MSG)
#
#     except FileNotFoundError as e:
#         print(str(e))
#
# with open(file_name) as file_handle:
#     for line in file_handle:
#
#         email_address_index = 1
#
#         line = line.rstrip()
#
#         if line.startswith('From:'):
#             line_starts_with_from_WORDS = line.split()
#             email_addresses.append(line_starts_with_from_WORDS[email_address_index])
#
#             # print(valid_line)
#             # print(line)
#         else:
#             continue
#
# for emai_address in email_addresses:
#     print(emai_address)
#
# count = len(email_addresses)
# print(f'There were {count} lines in the file with From as the first word')

# Chat GPT solution 1:  There is something wrong with this solution

# filename = 'your_file.txt'  # Replace 'your_file.txt' with the actual file name
#
# try:
#     with open(filename, 'r') as file:
#         count = 0
#         for line in file:
#             if line.startswith('From '):
#                 count += 1
#                 words = line.split()
#                 print(words[1])
#
#         print(f"\nTotal count: {count}")
#
# except FileNotFoundError:
#     print(f"Error: File '{filename}' not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# Chat GPT solution 2:

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
#
# try:
#     fh = open(fname)
#     count = 0
#
#     for line in fh:
#         if line.startswith('From '):
#             count += 1
#             words = line.split()
#             print(words[1])
#
#     print("There were", count, "lines in the file with 'From' as the first word")
#
# except FileNotFoundError:
#     print(f"Error: File '{fname}' not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     fh.close()




# Chat GPT solution 3:

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
#
# try:
#     with open(fname, 'r') as fh:
#         count = 0
#
#         for line in fh:
#             if line.startswith('From '):
#                 count += 1
#                 words = line.split()
#                 print(words[1])
#
#         print("There were", count, "lines in the file with 'From' as the first word")
#
# except FileNotFoundError:
#     print(f"Error: File '{fname}' not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
