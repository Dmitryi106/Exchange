from func import format_operation, sorted_list, new_list
from utils import data

new_list(data)
new_list = new_list(data)

sorted_list(new_list)
sorted_list = sorted_list(new_list)


def get_print():

    for i in range(5):
        print(format_operation(sorted_list[i]))
        print('')
    return


get_print()