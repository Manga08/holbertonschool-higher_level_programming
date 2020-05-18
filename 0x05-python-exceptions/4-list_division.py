#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for ct in range(0, list_length):
        try:
            l = 0
            l = my_list_1[ct] / my_list_2[ct]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(l)
    return new_list
