# Correct the following code

# han = open('mbox-short.txt')
#
# for line in han:
#     line = line.rstrip()
#     wds = line.split()
#     if wds[0] != 'From' :
#         continue
#     print(wds[2])

############
# Solution 1:

# han = open('mbox-short.txt')
#
# for line in han:
#     line = line.rstrip()
#     # print('Line:', line)
#     wds = line.split()
#     # print('Words: ', wds)
#     # Gaurdian method
#     if len(wds) < 3: # changed from 1 to 3
#         continue
#     if wds[0] != 'From':
#         # print('Ignore')
#         continue
#     print(wds[2])

# Solution 2:

# han = open('mbox-short.txt')
#
# for line in han:
#     line = line.rstrip()
#     # print('Line:', line)
#     if line == '':
#         # print('Skip Blank')
#         continue
#     wds = line.split()
#     # print('Words: ', wds)
#     if wds[0] != 'From':
#         # print('Ignore')
#         continue
#     print(wds[2])

# Solution 3:

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print('Line:', line)
    wds = line.split()
    # print('Words: ', wds)
    # Gaurdian method
    if (len(wds) < 3) or wds[0] != 'From': # This statement is one directional, switching the 'or' conditions around will cause this program to fail
        # print('Ignore')
        continue
    print(wds[2])
