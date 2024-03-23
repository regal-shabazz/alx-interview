#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    current = 1
    initial = 0
    count = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            initial = current
            current += initial
            count += 2
        else:
            current += initial
            count += 1
    return count
