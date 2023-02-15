
    try:
        score = float(input("Enter Score between 0 and 1: "))
        if 0 <= score <= 1:
        else:
            raise ValueError
    except ValueError:
        print('Invalid value input, value must be a decimal value between 0 and 1')

print(score)
