
# def sum_numbers(any_list):
    
#     summa=0
#     for element in any_list:
#         if type(element) == int or type(element) == float:
#             summa += element
            

#     return summa

def sum_numbers(any_list):
    import numbers
    def is_number(item):
        return isinstance(item, numbers.Number)
    summ=0
    for element in any_list:
        if is_number(element) == True:
            summ += element

    return summ
    