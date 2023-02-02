import socket


def is_valid_IP(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        return False


def is_valid_IP_2(strng):
    if len(strng.split(".")) != 4:
        return False

    for group in strng.split("."):
        if not group.isdigit() or group != str(int(group)) or not 0 <= int(group) <= 255:
            return False

    return True


import ipaddress


def is_valid_IP_3(strng):
    try:
        ipaddress.ip_address(strng)
        return True
    except:
        return False;
