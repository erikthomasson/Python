tupl1=(1,2,3,4)
tupl2=(3,4,5,6,7)
newtupl=()

for stuff in tupl1:
    if stuff not in tupl2:
        newtupl += (stuff,)
for stuff in tupl2:
    if stuff not in tupl1 and stuff not in newtupl:
        newtupl += (stuff,)


print(newtupl)