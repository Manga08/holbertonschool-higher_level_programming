#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return[replace if num_comp == search else num_comp for num_comp in my_list]
