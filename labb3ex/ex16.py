

dic= {'a':3, 'b':3, 'c':3}
newdict={}

for stuff in dic:
    print(dic[stuff])
    if dic[stuff] not in newdict:
        newdict[dic[stuff]] = list(stuff)  
    else:
        newdict[dic[stuff]] += list(stuff)

print(newdict)








