#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not len(list_of_integers) > 0:
        return None
    else:
        if len(list_of_integers) == 1:
            return list_of_integers[0]

        med = len(list_of_integers) / 2
        med = int(med)

        if len(list_of_integers) == 2:
            if list_of_integers[med] > list_of_integers[0]:
                return list_of_integers[med]
            else:
                return list_of_integers[0]

        if (list_of_integers[med] > list_of_integers[med - 1] and
                list_of_integers[med] > list_of_integers[med + 1]):
            return list_of_integers[med]

        if list_of_integers[med + 1] > list_of_integers[med]:
            return find_peak(list_of_integers[med + 1:])

        return find_peak(list_of_integers[0:med])
