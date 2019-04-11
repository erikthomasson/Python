
gal1=[]
diction= {0:1,2:1,4:2,6:1,9:1}
störst=0
for stuff in diction:
    if stuff > störst:
        störst = stuff

for num in range(stuff +1):
    if num in diction.keys():
        gal1.append(diction[num])
    else:
        gal1.append(0)
print(gal1)


