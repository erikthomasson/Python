num = int(input('Fibonacci calc. Enter a number: '))
if num == 0:
    print('0')
elif num == 1:
    print('1')
elif num -1 == 1 and num - 2 == 0:
    print((num - 1) + (num - 2))
else:
    print((num - 1) + (num - 2) - 1)