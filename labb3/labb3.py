# Erik Thomasson
#3A
def range_product(n_min,n_max):
    '''Produkten av alla heltal från n_min till n_max. Av Erik Thomasson'''
    if n_min == n_max:
        return n_min
    return n_min * range_product(n_min+1,n_max)


#3B
def dictionary_of_words_in_file(file):
    '''Hur många gånger varje ord i en fil uppkommer. Av Erik Thomasson'''
    with open(file) as x:
        diction={}
        for lines in x:
            index=0
            while index < len(lines.split()):
                if lines.split()[index] not in diction:
                    diction[lines.split()[index]] = 1
                else: 
                    diction[lines.split()[index]] += 1
                index+=1
    return diction

    
'''De 10 mest frekventa orden i en fil'''
fulldict = dictionary_of_words_in_file('Alice.txt')
top10keys=[]
for keys in fulldict.values():
    top10keys.append(keys)
    top10keys.sort()

top10keys = top10keys[::-1]
top10keys = top10keys[:10]
newdict={}

for keys in fulldict:
    index=0
    while index < 10 and len(newdict) < 10:
        if fulldict[keys] == top10keys[index]:    
            newdict[top10keys[index]] = keys
        index+=1
#print(newdict)
print('Word  : Occurances')
index= 0
stop = False
while stop == False:
    
    for keys in fulldict:

        if index == 10:
            stop = True
            break
        if fulldict[keys] == top10keys[index]:    
            print(f'{keys:5} : {top10keys[index]}')

            index+=1
