
strings = ('al', 'bal','cal')
stigande=()
minsta= 'z' 
for word in strings:
    if word <= minsta:
        minsta= word

stigande += (minsta,)
print(minsta)
strings = strings - minsta
print(strings)
