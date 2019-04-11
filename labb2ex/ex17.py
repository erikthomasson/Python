
def add_first_and_last(num_list):
    if len(num_list) == 1:
        num = num_list[0]
    elif num_list == []:
        num=0
    else:
        num= num_list[0] + num_list[len(num_list) -1]
    return num


