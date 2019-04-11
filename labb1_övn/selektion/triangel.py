def is_isosceles(x, y, z):
    if x == y or x == z or y == z and x>0 and z>0 and y>0:
        print('True')
    else:
        print('False')
    return