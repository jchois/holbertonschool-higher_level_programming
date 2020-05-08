#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or len(roman_string) is 0:
        return 0
    roman = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000
    }
    res = 0
    prev = 0
    cycle = 0
    for roman_k in roman_string:
        if cycle > 0 and prev < roman[roman_k]:
            res -= prev
            res = res + (roman[roman_k] - prev)
        else:
            res = res + roman[roman_k]
        cycle += 1
        prev = roman[roman_k]
    return res
