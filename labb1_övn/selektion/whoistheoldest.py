name1 = input('Person1 whats your name? :')
birth1 = int(input('and what year were u born? :'))
name2 = input('Now person2 whats your name? :')
birth2 = int(input('and what year were u born? :'))
age1 = 2018 - birth1
age2 = 2018 - birth2
if birth1>2018 and birth1<1900 and birth2>2018 and birth2<1900:
    print(name1, 'and/or', name2, 'please enter a number between 1900 and 2018')
else:
    print('Hello', name1, 'and', name2, 'ur age is', age1, 'and', age2)
if age1 > age2:
    print(name1, 'you are the oldest')
else:
    print(name2, 'you are the oldest')
