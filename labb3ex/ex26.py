


def func(word):
    if word=="":
        return None
    if len(word) == 1:
        return word 
    print(word)
    return func(word[0]) + '-' + func(word[1:])
print(func('duck'))



