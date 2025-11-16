def solution(roman: str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    roman_as_int = 0

    roman_numeral_1s = {'I': 1,
                        'X': 10,
                        'C': 100,
                        'M': 1000}
    roman_numeral_5s = {'V': 5,
                        'L': 50,
                        'D': 500}

    for i in roman:
        roman_as_int += i

    return roman_as_int


if __name__ == '__main__':
    # print('MMMDCCCLXXXVIII'.split())

    sample = 'MMMDCCCLXXXVIII'

    for i in sample:
        print(i)
