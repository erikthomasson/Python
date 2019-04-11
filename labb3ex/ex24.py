def sum(tal):    
    
    tal= str(tal)
    if tal == "":
        return 0 
    return int(tal[0]) + sum(tal[1:])
print(sum(111))