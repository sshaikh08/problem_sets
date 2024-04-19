"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the
counts for each hour, print out the counts, sorted by hour as shown below."""

# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from
# the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the
# counts for each hour, print out the counts,
# sorted by hour as shown below.

# Starting Code

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# My Updated Solution
FILE_NOT_FOUND_ERR_MSG = "Error: File not found. Please enter a valid file path."

email_counts_each_hour = dict()
hours_emails_sent = list()

while True:
    try:
        filename = input("Enter file name: ") or "mbox-short.txt"

        with open(filename) as file_handle:
            for line in file_handle:
                if line.startswith('From '):

                    hour_email_sent = line.split()[-2][0:2]
                    print(f"{hour_email_sent}")

                    hours_emails_sent.append(hour_email_sent)

        break
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERR_MSG)

print("\n")

for hour in sorted(hours_emails_sent):
    email_counts_each_hour[hour] = email_counts_each_hour.get(hour, 0) + 1

for hour, count in email_counts_each_hour.items():
    print(hour, count)

# My Solution GPT 4 optimized

# times_emails_sent = list()
#
# while True:
#     try:
#         file_name = input('Please enter a text file: ')
#         if len(file_name) < 1:
#             file_name = 'mbox-short.txt'
#         with open(file_name) as file_handle:
#             for line in file_handle:
#                 if line.startswith('From') and len(line.split()) > 2:
#                     time_email_sent = line.rstrip().split()[-2]
#                     times_emails_sent.append(time_email_sent)
#         break
#
#     except FileNotFoundError:
#         print('The file you entered does not exist. Please enter a valid file name.')
#
# hours_distribution = dict()
#
# for instance in times_emails_sent:
#     hour = instance.split(':')[0]
#     hours_distribution[hour] = hours_distribution.get(hour, 0) + 1
#
# sorted_hours = sorted(hours_distribution.items())
#
# for hour, count in sorted_hours:
#     print(hour, count)


# GPT 4 Solution (Slightly edited by me)


# while True:
#     try:
#         file_name = input('Please enter a text file: ')
#         if len(file_name) < 1:
#             file_name = 'mbox-short.txt'
#         with open(file_name, "r") as file:
#             hour_counts = dict()
#
#             for line in file:
#                 if line.startswith("From "):
#                     time = line.split()[5]
#                     hour = time.split(":")[0]
#                     hour_counts[hour] = hour_counts.get(hour, 0) + 1
#
#         break
#     except FileNotFoundError:
#         print(f"File '{file_name}' not found. Please make sure the file is in the same directory as this script.")
# sorted_counts = sorted(hour_counts.items())
#
# for hour, count in sorted_counts:
#     print(f"{hour}: {count}")

# My Solution

times_emails_sent = list()

while True:
    try:
        file_name = input('Please enter a text file: ')
        if len(file_name) < 1:
            file_name = 'mbox-short.txt'
        with open(file_name) as file_handle:
            for line in file_handle:
                if line.startswith('From') and (len(line.split()) > 2):
                    time_email_sent = line.rstrip().split()[-2:-1][0]
                    times_emails_sent.append(time_email_sent)

        break

    except FileNotFoundError:
        print('The file you entered does not exist. Please enter a valid file name.')

hours_distribution = dict()

for instance in times_emails_sent:
    hour_min_sec = instance.split(':')
    hour = hour_min_sec[0]
    hours_distribution[hour] = hours_distribution.get(hour, 0) + 1

hour_list = list()
for key, value in hours_distribution.items():
    hour_and_count = (key, value)
    hour_list.append(hour_and_count)

for hour_and_count in sorted(hour_list):
    hour = hour_and_count[0]
    count = hour_and_count[1]
    print(hour, count)



