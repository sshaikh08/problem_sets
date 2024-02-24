

# Starting code:

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# My Final Solution

emails = dict()

while True:
    try:
        filename = input("Enter file name: ") or "mbox-short.txt"


        with open(filename) as file:
            for line in file:
                if line.startswith('From '):
                    email = line.split()[1]
                    emails[email] = emails.get(email, 0) + 1

        break
    except FileNotFoundError:
        print("Error: File not found. Please enter a valid file path.")

max_count = max(emails.values())
max_email = max(emails, key=emails.get)

just_emails = emails.values()

print(max_email, max_count)

# My Original Solution:

# while True:
#     try:
#         name = input("Enter file:")
#         if len(name) < 1:
#             # name = "mbox-short.txt"
#             name = 'py4e_assignments/8-lists/mbox-short.txt'
#
#         email_address_list = list()
#
#         with open(name) as handle:
#             for line in handle:
#                 if not line.startswith('From:'):
#                     continue
#                 line.rstrip()
#                 email_address = line.split()[1]
#                 email_address_list.append(email_address.rstrip())
#         break
#     except FileNotFoundError:
#         print('File not found. Please enter a valid file path.')
#
# # print(email_address_list)
#
# email_addresses = dict()
#
# for email_address in email_address_list:
#     email_addresses[email_address] = email_addresses.get(email_address, 0) + 1
#
# # print(email_addresses)
# most_emails_sent = -1
# email_that_sent_most = None
# for email_address, number_of_emails_sent in email_addresses.items():
#     if number_of_emails_sent > most_emails_sent:
#         most_emails_sent = number_of_emails_sent
#         email_that_sent_most = email_address
#
# print(email_that_sent_most, most_emails_sent)






# Chat GPT Solution

# filename = input("Enter file name: ") or "mbox-short.txt"
#
# emails = dict()
# try:
#     with open(filename) as file:
#         for line in file:
#             if line.startswith('From '):
#                 email = line.split()[1]
#                 emails[email] = emails.get(email, 0) + 1
#
#     max_count = max(emails.values())
#     max_email = max(emails, key=emails.get)
#
#     print(max_email, max_count)
#
# except FileNotFoundError:
#     print("Error: File not found.")
