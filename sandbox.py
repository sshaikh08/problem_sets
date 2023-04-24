

with open('mbox-short.txt') as file:
    for line in file:
        if line.startswith('From:'):
            print(line.rstrip())
            print(line.find('From:'))


