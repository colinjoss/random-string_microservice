import random as rd
import math


UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIALS = '@%+!$$?~'


def generate_random_string(length, upper, number, special):
    """
    Returns random string of a given length with/without uppercase letters,
    numbers, or special characters.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz'
    if upper:
        chars += UPPERS
    if number:
        chars += NUMBERS
    if special:
        chars += SPECIALS

    password = ''
    for i in range(0, length):
        password += chars[math.floor(rd.random() * len(chars))]

    return password
