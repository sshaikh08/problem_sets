
# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of
# range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table: Score Grade >=
# 0.9 A >= 0.8 B >= 0.7 C >= 0.6 D < 0.6 F If the user enters a value out of range, print a suitable error message
# and exit. For the test, enter a score of 0.85.

# My Submission
try:
    Grade = float(input("Enter Grade between 0 and 1: "))
    if not 0 <= Grade <= 1:
        raise ValueError
    if Grade >= 0.9:
        print('A')
    elif 0.9 > Grade >= 0.8:
        print('B')
    elif 0.8 > Grade >= 0.7:
        print('C')
    elif 0.7 > Grade >= 0.6:
        print('D')
    elif 0.6 > Grade:
        print('F')
except ValueError:
    print('Invalid value input, value must be a decimal value between 0 and 1')

############
# Optimized Solution

try:
    grade_str = input("Enter grade between 0 and 1: ")
    grade = float(grade_str)
    if not 0 <= grade <= 1:
        raise ValueError
    if grade >= 0.9:
        print('A')
    elif grade >= 0.8:
        print('B')
    elif grade >= 0.7:
        print('C')
    elif grade >= 0.6:
        print('D')
    else:
        print('F')
except ValueError:
    print('Invalid value input, value must be a decimal value between 0 and 1')





