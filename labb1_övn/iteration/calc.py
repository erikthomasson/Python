def calc():
    print('Now what do you want to do?')
    print('')
    print('1. Enter two new integers')
    print('2. Add')
    print('3. Subtract')
    print('4. Muliply')
    print('5. Divide')
    print('0. Exit')


print('1. Enter two integers')
print('2. Add')
print('3. Subtract')
print('4. Muliply')
print('5. Divide')
print('0. Exit')
a = int(input('Your choice: '))
while a != 0: 
    int1 = 0
    int2 = 0
    while a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 0:
        if a == 1:
            int1 = int(input())
            int2 = int(input())
            a = int(input('What do you want to do with those numbers?: '))
        
        if a == 2 and int1 != 0 and int2 != 0:
            print('=', int1 + int2)
            calc()
            a = int(input())
        
        if a == 3 and int1 != 0 and int2 != 0:
            print(int1, "-", int2, '=', int1 - int2)
            calc()
            a = int(input())
        
        if a == 4 and int1 != 0 and int2 != 0:
            print('=', int1 * int2)
            calc()
            a = int(input())
        
        if a == 5 and int1 != 0 and int2 != 0:
            print('=', int1 / int2)
            calc()
            a = int(input())
        if a == 0:
            break
        print('You need to submit two integers')
        a = 1
if a != 0:
    print('Input must be either 0,1,2,3,4 or 5.')
    print('')
    print('1. Enter two integers')
    print('2. Add')
    print('3. Subtract')
    print('4. Muliply')
    print('5. Divide')
    print('0. Exit')
    a = int(input('Your choice: '))
            
            
