# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for
# lines of the form: X-DSPAM-Confidence:    0.8475 Count these lines and extract the floating point values from each
# of the lines and compute the average of those values and produce an output as shown below. Do not use the sum()
# function or a variable named sum in your solution. You can download the sample data at
# http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Starting Code:
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     print(line)
# print("Done")


# My Solution:


# Use the file name mbox-short.txt as the file name
SPAM_CONFIDENCE_STRING = 'X-DSPAM-Confidence: '
fname = input("Enter file name: ")
fh = open(fname)

spam_confidence_total = 0
count = 0
for line in fh:
    if not line.startswith(SPAM_CONFIDENCE_STRING):
        continue
    # print(line)
    spam_confidence_total += float(line.lstrip(SPAM_CONFIDENCE_STRING))
    count += 1

average_spam_confidence = spam_confidence_total / count
# print(f'Count: {count}')
# print(f'Spam Confidence Total: {spam_confidence_sum}')
print(f'Average spam confidence: {average_spam_confidence}')
# print("Done")

# Chat GPT Optimized Solution 1:
SPAM_CONFIDENCE_STRING = 'X-DSPAM-Confidence: '
fname = input("Enter file name: ")

with open(fname) as fh:
    spam_confidence_total = 0
    count = 0
    for line in fh:
        if not line.startswith(SPAM_CONFIDENCE_STRING):
            continue
        try:
            spam_confidence_total += float(line[len(SPAM_CONFIDENCE_STRING):])
            count += 1
        except ValueError:
            pass

    if count > 0:
        average_spam_confidence = spam_confidence_total / count
       # print(f'Average spam confidence: {average_spam_confidence:.12f}')
        print(f'Average spam confidence: {average_spam_confidence}')
    else:
        print('No lines starting with "X-DSPAM-Confidence: " found in the file.')

# Chat GPT Optimized Solution 2:
# SPAM_CONFIDENCE_STRING = 'X-DSPAM-Confidence: '
# fname = input("Enter file name: ")
# count = 0
# total = 0
#
# with open(fname) as fh:
#     for line in fh:
#         if line.startswith(SPAM_CONFIDENCE_STRING):
#             count += 1
#             value = float(line[len(SPAM_CONFIDENCE_STRING):])
#             total += value
#
# if count > 0:
#     average = total / count
#     print(f'Average spam confidence: {average:.12f}')
# else:
#     print('No lines starting with "X-DSPAM-Confidence: " found in the file.')

