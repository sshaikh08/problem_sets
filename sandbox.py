
# My Original Solution:

while True:
    try:
        name = input("Enter file:")
        if len(name) < 1:
            # name = "mbox-short.txt"
            name = 'py4e_assignments/8-lists/mbox-short.txt'

        email_address_list = list()

        with open(name) as handle:
            for line in handle:
                if not line.startswith('From:'):
                    continue
                line.rstrip()
                email_address = line.split()[1]
                email_address_list.append(email_address.rstrip())
        break
    except FileNotFoundError:
        print('File not found. Please enter a valid file path.')

# print(email_address_list)

email_addresses = dict()

for email_address in email_address_list:
    email_addresses[email_address] = email_addresses.get(email_address, 0) + 1

# print(email_addresses)
most_emails_sent = -1
email_that_sent_most = None
for email_address, number_of_emails_sent in email_addresses.items():
    if number_of_emails_sent > most_emails_sent:
        most_emails_sent = number_of_emails_sent
        email_that_sent_most = email_address

print(email_that_sent_most, most_emails_sent)