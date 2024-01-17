# import os.path as path
#
# print(path.isfile('mbox-short.txt'))

email_counts_each_hour = dict()
hours_emails_sent = list()

while True:
    try:
        filename = input("Enter file name: ") or "mbox-short.txt"

        with open(filename) as file_handle:
            for line in file_handle:
                if line.startswith('From '):

                    hour_email_sent = line.split()[-2][0:2]

                    hours_emails_sent.append(hour_email_sent)

        break
    except FileNotFoundError:
        print("Error: File not found. Please enter a valid file path.")

for hour in sorted(hours_emails_sent):
    email_counts_each_hour[hour] = email_counts_each_hour.get(hour, 0) + 1

for hour, count in email_counts_each_hour.items():
    print(hour, count)


# print(email_counts_each_hour)
# print(hours_emails_sent)

# for hour, count in sorted(email_counts_each_hour):
#     print(hour,count)

# for hour, count in email_counts_each_hour.items():
#     email_counts_each_hour[hour] = email_counts_each_hour.get(hour, 0) + 1

# print(type(sorted(email_counts_each_hour)))


