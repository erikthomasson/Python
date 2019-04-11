print('This program prints out a multiplication table')
num = int(input('Enter a number: '))
for x in range(0, 10):
    b = x * num
    print(x, '*', num, '=', b)