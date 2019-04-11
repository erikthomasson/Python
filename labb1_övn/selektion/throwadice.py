import random
print('Welcome to the dice game')
player1 = input('Player1 whats your name? :')
player2 = input('Player2 Whats your name? :')
random1 = random.randint(1,6)
random2 = random.randint(1,6)
print(player1 + ', your dice shows', random1)
print(player2 + ', your dice shows', random2)
if random1 < random2:
    print('Winner is', player2)
elif random1 > random2:
    print('Winner is', player1)
else:
    print('No one wins')