# DO NOT RUN CODE. RUN EACH BLOCK IN SANDBOX ENVIRONMENT

# Regular Expressions Examples


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')

print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
###########################################

# Double Split Patten
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

############################################

# Regex Version 1
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', line)
print(y)

##############################################

# Regex Version 2

import re
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', line)
print(y)

#################################################

#Example Program
import re
with open('mbox-short.txt') as hand:
    numlist = list()
    for line in hand:
        line = line.rstrip()
        stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
        if len(stuff) != 1 : continue
        num = float(stuff[0])
        numlist.append(num)
print('Maximum:', max(numlist))

#####################################################

#Regex Example 2

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
