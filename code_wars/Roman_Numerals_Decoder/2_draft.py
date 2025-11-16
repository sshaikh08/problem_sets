# # Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.
#
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is
# rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "M"       -> 1000
# "CM"      ->  900
# "CD"      ->  400
# "XC"      ->   90
# "XL"      ->   40
# "IX"      ->    9
# "IV"      ->    4
# "I"       ->    1


# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solution(roman: str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""

    roman_as_int = 0

    roman_numerals = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}

    roman_numerals_4s_and_9s = {'IV': 4,
                                'IX': 9,
                                'XL': 40,
                                'XC': 90,
                                'CD': 400,
                                'CM': 900}

    # noinspection PyShadowingNames
    for i in reversed(roman):
        roman_as_int += roman_numerals[i]

    return roman_as_int


############################################################################################

# noinspection SpellCheckingInspection
if __name__ == '__main__':
    # print('MMMDCCCLXXXVIII'.split())

    sample = 'XL'

    sample_first_value = sample.split()[0]
    sample_second_value = sample.split()[1]

    roman_numerals_test = {'I': 1,
                           'V': 5,
                           'X': 10,
                           'L': 50,
                           'C': 100,
                           'D': 500,
                           'M': 1000}

    test_1 = False
    if test_1:
        for i in sample:
            print(i)

    test_2 = False
    if test_2:
        print(roman_numerals_test['M'])

    test_3 = False
    if test_3:
        print(solution(sample))

    test_4 = False
    if test_4:
        print(f"Index of last roman value: {list(roman_numerals_test).index(sample_first_value)}")
