# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
# they consist of four octets, with values between 0 and 255, inclusive.


# Optimal solution:

def is_valid_IP(s):
    return s.count('.') == 3 and all(o.isdigit() and 0 <= int(o) <= 255 and str(int(o)) == o for o in s.split('.'))


# The following is how I would have made this a little more readable

def is_valid_IP_shariq(ipAddress_to_check):
    periods_in_ipAddress = 3
    min_octet_value = 0
    max_octet_value = 255
    periods_in_input = ipAddress_to_check.count('.')
    are_all_octets_valid = all(
        i.isdigit() and min_octet_value <= int(i) <= max_octet_value and str(int(i)) == i for i in
        ipAddress_to_check.split('.'))

    is_IPAddress_Valid = (periods_in_input == periods_in_ipAddress) and are_all_octets_valid

    # print(periods_in_input)
    # print(periods_in_ipAddress)
    # print(are_all_octets_valid)
    # print((periods_in_input == periods_in_ipAddress) and are_all_octets_valid)

    return is_IPAddress_Valid
