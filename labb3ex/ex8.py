
tuplsort=()
lista= [(1, 'Welcome'),(2,'to'),(4,'Python'),(3,'the'),(5, 'course')]
index = 1
while index <= len(lista):
    for i in lista:
        if i[0] == index:
            tuplsort += (i[1],) 
    index+=1        

print(tuplsort) 