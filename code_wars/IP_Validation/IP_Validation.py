# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
# they consist of four octets, with values between 0 and 255, inclusive.


# Optimal solution:

def is_valid_IP(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))
