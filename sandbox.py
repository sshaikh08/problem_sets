# 3.3 (Should Probably be 3.2) Write a program to prompt for a score between 0.0 and 1.0. If the score is out of
# range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table: Score Grade >=
# 0.9 A >= 0.8 B >= 0.7 C >= 0.6 D < 0.6 F If the user enters a value out of range, print a suitable error message
# and exit. For the test, enter a score of 0.85.
try:
    score = float(input("Enter Score between 0 and 1: "))
    if not 0 <= score <= 1:
        raise ValueError

except ValueError:
    print('Invalid value input, value must be a decimal value between 0 and 1')

print(score)
