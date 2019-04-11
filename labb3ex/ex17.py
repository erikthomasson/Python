

lista=[1,0,1,0,2,0,1,0,0,1,0]
count=0
diction={}
for num in lista:
    if num != 0:
        diction[count] = num

    count +=1

print(diction)