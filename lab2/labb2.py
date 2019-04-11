'''A mastermind game with numbers instead of colours by Erik Thomasson'''

import random
listofnumbers= ['0','1','2','3','4','5','6','7','8','9']
num1 = random.choice(listofnumbers)
listofnumbers.remove(num1)

num2 = random.choice(listofnumbers)
listofnumbers.remove(num2)

num3 = random.choice(listofnumbers)
listofnumbers.remove(num3)

num4 = random.choice(listofnumbers)

listofnumbers= ['0','1','2','3','4','5','6','7','8','9']

secretnumber= num1 + num2 + num3 + num4
print('This mastermind game uses a 4-digit sequence.\nThe numbers can be 0-9 in all of the positions.\nThe same number cannot occur twice')

guess= 'This is not the secret number yet...'
tries=0
while guess != secretnumber:
    guess= input('Guess the 4-digit sequence: ')
    index=0
    rightplace=0
    rightnumber=0
    tries+=1
    for num in secretnumber:

        if guess[index] == secretnumber[index]:
            rightplace +=1

        elif guess[index] in secretnumber:
            rightnumber +=1
        index +=1
    print('The amount of right number(s) in the right position:', rightplace, 'The amount of right number(s) but in the wrong position:', rightnumber)

print(f'It took you {tries} tries to get the right sequence')
