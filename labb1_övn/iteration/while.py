age = 25
num = 0
while num < age:
    if num == 0:
        num += 1
        continue #continue betyder att man går tillbaka till while()
    if num % 2 == 0:
        print(num)
    if num > 10:
        break #betyder att man hoppar och fortsätter m koden (detta fall 12)
    num += 1
