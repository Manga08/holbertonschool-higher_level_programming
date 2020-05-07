#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    op = 0

    for ct in range(0, len(roman_string)):
        if ct > 0 and Dict[roman_string[ct]] > Dict[roman_string[ct - 1]]:
            op += Dict[roman_string[ct]] - Dict[roman_string[ct - 1]] * 2
        else:
            op += Dict[roman_string[ct]]
    return op
