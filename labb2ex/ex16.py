


def sum_last_digits(int_list):
# numbers = [123, 23, 541, 2, 1]
    nums = 0
    for num in int_list:
        nums += (num % 10)
    return nums


