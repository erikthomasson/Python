dic= {"c":1, "b":2, "a":1}
value= 1
lista = []
for grejer in dic:
    if dic[grejer] == value:
        lista.append(grejer)
        print(lista)
lista.sort()
print(lista)


