

def func(x,y):
    if x == y:
        return x
    return str(x) + ',' + str(func(x + 1,y))

print(func(2,5))
