emails = dict()

while True:
    try:
        filename = input("Enter file name: ") or "mbox-short.txt"

        with open(filename) as file:
            for line in file:
                print(line)

        break
    except FileNotFoundError:
        print("Error: File not found. Please enter a valid file path.")