


def func(n):
    if n == 0:
        return '*'
    if n ==1:
        return '**'
    return '**' + func(n-1)

print(func(3))


