#!usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list) - 1:
        return (None)
    else:
        for i in my_list:
            if idx == my_list.index(i):
                return (i)
