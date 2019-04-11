def max2(num1, num2):
    if num1 < num2:
        print(num2)
    else:
        print(num1)
    return


''' Maximum version 2'''
def max3(num1, num2, num3):
    if num1 < num2 < num3:
        print(num3)
    elif num2 < num1 < num3:
        print(num3)
    elif num2 < num3 < num1:
        print(num1)
    elif num3 < num2 < num1:
        print(num1)
    elif num1 < num3 < num2:
        print(num2)
    elif num3 < num1 < num2:
        print(num2)
    else:
        print('error')

