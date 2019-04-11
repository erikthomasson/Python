#print('hallå')
try:

    a = int(input('variabel a: '))
    b= int(input('variabel b: '))

    print(a/b)
except ZeroDivisionError:
    print('learn some math you cant divide by 0')

except ValueError:
    print('use a int')