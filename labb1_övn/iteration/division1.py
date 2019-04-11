print('This program sums all numbers between 2 given numbers')
num1 = int(input('sum from this number'))
num2 = int(input('to this number'))

b = 0
for x in range(num1,num2 + 1):
    if x % 3 == 0:
        b += x
    if x == num2:
        print(b)
    
a = 0
for x in range(1,2000):
    if x % 3 == 0 or x % 7 == 0:
        a += x
    if x == 1999:
        print(a)
