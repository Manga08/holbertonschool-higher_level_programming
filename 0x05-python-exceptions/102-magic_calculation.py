#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for ct in range(1, 3):
        try:
            if ct > a:
                raise Exception('Too Far')
            else:
                result += a ** b / ct
        except:
            result = a + b
            break
    return result
