tupl1=(1,2,3)
tupl2=(2,5,1)
index=0
newtupl=()
while len(tupl2) > index:
    for stuff in tupl1:
        if stuff == tupl2[index]:
            newtupl += (stuff,)
    index+=1
print(newtupl)



