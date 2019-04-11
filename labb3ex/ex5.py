
tupl1= (1,2)
tupl2= (1,2)
result= False
right = False
index=0
while len(tupl1) == len(tupl2) and index < len(tupl2):
    for num in tupl1:
        if num == tupl2[index]:
            right= True
            break
    if right == False:
        result= False
        break
    result = True
    index += 1
print(result)




