# Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fh = open('mbox-short.txt')

# print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

fh.close()
