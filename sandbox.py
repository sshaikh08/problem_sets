# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be
# the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put
# the logic to do the computation of pay in a function called computepay() and use the function to do the
# computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the
# pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not
# worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do
# not name your variable sum or use the sum() function.


INVALID_INPUT_ERR_MSG = "Please enter a valid number greater than 0."
INVALID_INPUT_FOR_HOURS_ERR_MSG = "Please enter a valid number greater than 0 for Hours."
INVALID_INPUT_FOR_RATE_ERR_MSG = "Please enter a valid number greater than 0 for Hourly Rate."


def computepay(hours_worked, hourly_rate):
    max_allowed_regular_hours = 40

    if hours > max_allowed_regular_hours:
        base_pay = hourly_rate * max_allowed_regular_hours

        overtime_hours = (hours - max_allowed_regular_hours)
        time_and_a_half = overtime_hours + (overtime_hours / 2)
        overtime_pay = hourly_rate * time_and_a_half

        final_pay = base_pay + overtime_pay
    else:
        final_pay = hours_worked * hourly_rate

    return final_pay


while True:
    try:
        hours = float(input('Enter Hours: '))
        if hours <= 0:
            raise ValueError(INVALID_INPUT_FOR_HOURS_ERR_MSG)
        rate = float(input('Enter Hourly Rate: '))
        if rate <= 0:
            raise ValueError(INVALID_INPUT_FOR_RATE_ERR_MSG)
        break

    except (ValueError, TypeError) as e:
        print(str(e))

final_pay = computepay(hours, rate)

print("Pay", final_pay)
