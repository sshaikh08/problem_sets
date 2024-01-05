# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
# split() method. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting
# words in python sort() order as shown in the desired output. You can download the sample data at
# http://www.py4e.com/code3/romeo.txt

# Original Instructor provided code to modify
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
# print(line.rstrip())



# My Final Optimized Solution
while True:
    try:
        fname = input("Enter file name: ")

        with open(fname) as fh:
            # Use set comprehension to create a set of unique words
            words = {word for line in fh for word in line.split()} # set comprehension

        break
    except FileNotFoundError:
        print('Invalid file entry. Please enter a valid file path.')

# Sort the words and convert the set to a list
sorted_words = sorted(words) # sorted() takes in *iterable* and returns a sorted list of the items in the iterable

print(sorted_words)

# My Solution

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     line_lst = line.split()
#     for word in line_lst:
#         if word not in lst:
#             lst.append(word)
#         else:
#             continue
# lst.sort()
# print(lst)
# fh.close()

# Chat GPT Optimized Solution 1
# fname = input("Enter file name: ")
# lst = []
# with open(fname) as fh:
#     for line in fh:
#         line_lst = line.split()
#         for word in line_lst:
#             if word not in lst:
#                 lst.append(word)
# lst.sort()
# print(lst)

# Chat GPT Optimized Solution 2
# fname = input("Enter file name: ")
#
# with open(fname) as fh:
#     # Use set comprehension to create a set of unique words
#     words = {word for line in fh for word in line.split()} # set comprehension
#
# # Sort the words and convert the set to a list
# sorted_words = sorted(words)
#
# print(sorted_words)



# Unaccepted Solution

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     # print(line.split())
#     lst += line.split()
# lst_set = set(lst)
# lst = list(lst_set)
# lst.sort()
# print(lst)
# fh.close()