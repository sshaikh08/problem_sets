# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly
# rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a
# rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and
# float() to convert the string to a number. Do not worry about error checking the user input - assume the user types
# numbers properly.

# Starting Code:

# hrs = input("Enter Hours:")
# h = float(hrs)



# My solution:

# hrs = float(input("Enter Hours: "))
# pay_rate = float(input('Enter Pay Rate Per Hour: '))
# over_time_pay = None
# regular_hours = None
#
# if hrs > 40:
#     over_time_hours = hrs - 40
#     regular_hours = hrs - over_time_hours
#     over_time_pay = pay_rate * 1.5 * over_time_hours
#
# final_pay = (regular_hours*pay_rate) + over_time_pay
# print(f'Pay: {final_pay}')

# ChatGPT Optimized Solution
hours = float(input("Enter Hours: "))
pay_rate = float(input('Enter Pay Rate Per Hour: '))

if hours > 40:
    overtime_hours = hours - 40
    regular_hours = hours - overtime_hours
    overtime_pay = pay_rate * 1.5 * overtime_hours
    final_pay = (regular_hours * pay_rate) + overtime_pay
else:
    final_pay = hours * pay_rate

print(f"Your final pay is: ${final_pay:.2f}")


# Review Solution:

# hrs = input("Enter Hours: ")
# rate = input("Enter Hourly rate: ")
# hrs_float = float(hrs)
# rate_float = float(rate)
# max_hours = 40
#
# overtime_multiplier = 1.5
#
# overtime_rate = rate_float*overtime_multiplier
#
# overtime_hrs = None
#
# reg_pay = None
# overtime_pay = None
# final_pay = None
#
#
# if hrs_float > max_hours:
#     overtime_hrs = float(hrs) - max_hours
#
#     reg_pay = max_hours*rate_float
#     overtime_pay = overtime_rate*overtime_hrs
#
#     final_pay = reg_pay + overtime_pay
#
# else:
#     final_pay = hrs_float*rate_float
#
# print(f"{final_pay:.2f}")