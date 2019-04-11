import random
random1 = random.randint(1, 100)
x = 0
num1 = int(input('Guess a number from 1 to 100: '))
x += 1
while True:
    if num1 > random1:
        num1 = int(input('Thats to high guess again: '))
        x += 1
    elif num1 < random1:
        num1 = int(input('Thats to low guess again: '))
        x += 1
    elif num1 == random1:
        print('You guessed right after', x, 'tries')
        game2 = input('Do you want to play again?(y/n) ')
        if game2 == 'y':
            x = 0
            num1 = int(input('Guess a number from 1 to 100: '))
            x += 1
            continue
        print('Bye, come again')
        break
    