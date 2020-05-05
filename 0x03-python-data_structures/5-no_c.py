#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_list = list(my_string)
        for i in new_list:
            if i in "cC":
                new_list.remove(i)
        my_string = "".join(new_list)
    return my_string
