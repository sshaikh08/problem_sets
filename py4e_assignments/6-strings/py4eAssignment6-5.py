# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line
# below. Convert the extracted value to a floating point number and print it out.

# My Work:

# text = "X-DSPAM-Confidence:    0.8475"
#
# num_in_text_at = text.find('0.8475')
#
# print(num_in_text_at)
#
# print(text[num_in_text_at:])
#
# print(float(text[num_in_text_at:]))


# My Solution:

# text = "X-DSPAM-Confidence:    0.8475"
#
# num_in_text_at = text.find('0.8475')
#
# print(float(text[num_in_text_at:]))

#############################################

# ChatGPT Solution:

# 1:

# num_str = text[text.find(':')+1:].rstrip() # use rstrip() instead of strip()
# num = float(num_str)
# print(num)

# 2:

import re

text = "X-DSPAM-Confidence:    0.8475"

pattern = r'\d+\.\d+' # pattern to match a floating-point number
match = re.search(pattern, text) # search for the pattern in the string
if match: # if the pattern is found
    num_str = match.group() # extract the matched substring
    num = float(num_str) # convert the substring to a floating-point number
    print(num)





