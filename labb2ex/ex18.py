old_list= [['kangar'], ['z'], ['f']]
def distribute(my_item, old_list):
    count = 0
    for index in old_list:
        stop = len(old_list)
        index.append(my_item)
        if count == stop:
            break
        count += 1
    print(old_list)



