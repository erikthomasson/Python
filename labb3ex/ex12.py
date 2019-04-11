def func(lista):
#lista = {"one":1, "two":2, "seven":6, "eight":9}
    print("--")
    #index=0

#for keys in lista:

#    print(keys, "-", lista[keys])

    
    if lista == {}:
        return print("--")
    element=list(lista.keys())[0]
    print(element, lista[element])
    lista.pop(element)
    return func(lista)


