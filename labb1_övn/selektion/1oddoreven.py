num = int(input('Write a number: '))

if num%4 == 0:
    print(num, 'can be divided by 4')
elif num % 2 == 0:
    print(num, 'is Even')
elif num % 2 != 0:
    print(num, 'is Odd')
else:
    print('Error')

number = int(input('Write a number that u want to divide: '))
divisor = int(input('Write a number to divide with: '))
if number % divisor == 0:
    print('Ur ratio is even')
elif number % divisor !=0:
    print('Ur ratio is not even')
else:
    print('Use numbers!')