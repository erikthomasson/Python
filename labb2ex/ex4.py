def search(string, substring):
    index = -1
    for letter in string:
        if letter == substring[0]:
            index +=1
            break
        index = index + 1
    
    return index


