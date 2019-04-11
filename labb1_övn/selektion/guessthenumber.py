import random
num = int(input('Say a number from 1-10: '))
random1 = random.randint(1, 10)
if num == random1:
    print('Yay you got the right number!!!')
else: 
    print('Better luck next time')

num1 = int(input('Now you set the range from which number? :'))
num2 = int(input('to which number :'))
thenum = int(input('now say a number between ' + str(num1) + ' and ' + str(num2) + ' :'))
random2 = random.randint(num1, num2)
if num1 == num2:
    print('Well that wasnt that hard')
elif thenum == random2:
    print('Yay you got it!')
else: 
    print('Better luck next time')