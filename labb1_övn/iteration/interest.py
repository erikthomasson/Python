money = int(input("What's your start capital? :"))
interest = int(input("What's the interest in procent? :"))
years = int(input("For how many years do you want to save your money? :"))
x = 0
interest = interest / 100 + 1
while years != x:
    money = money * interest
    x += 1
print(money)



