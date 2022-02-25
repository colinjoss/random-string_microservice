import random as rd
import math
import rpyc


LOWERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIALS = '!@#$%^&*'


def generate_random_string(length, upper, number, special):
    chars = ''
    chars += LOWERS
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
