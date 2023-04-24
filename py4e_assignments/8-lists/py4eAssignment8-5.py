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