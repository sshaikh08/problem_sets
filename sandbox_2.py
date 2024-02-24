# import os.path as path
#
# print(path.isfile('mbox-short.txt'))
while True:
    try:
        name = input("Enter file name: ")  # Prompt user for file name
        if len(name) < 1:
            name = "mbox-short.txt"  # Default file name if user enters nothing

        email_addresses = {}  # Initialize an empty dictionary to store email addresses and their counts

        with open(name) as handle:  # Open the file
            for line in handle:  # Iterate over each line in the file
                if line.startswith("From "):  # Check if the line starts with "From "
                    email_address = line.split()[1]  # Extract the email address from the line
                    email_addresses[email_address] = email_addresses.get(email_address, 0) + 1  # Increment the count for the email address

        break  # Exit the loop if the file was found

    except FileNotFoundError:  # Handle the case when the file is not found
        print("File not found. Please enter a valid file name.")

# Find the email address with the highest count
max_count = max(email_addresses.values())  # Get the maximum count of emails sent
sender_with_max_emails = [
    email_address for email_address, count in email_addresses.items() if count == max_count
]  # Find all email addresses with the maximum count

# Print the email address with the highest count and the number of emails sent
print(
    f"Email address with the highest number of emails sent: {sender_with_max_emails[0]}"
)  # Print the email address with the maximum count
print(f"Number of emails sent: {max_count}")  # Print the maximum count of emails sent
