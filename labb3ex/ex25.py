
def func(word):

    if word== '':
        return 0
    if word[0] == 'X':
        word = word[1:]
        return func(word) +1
    word = word[1:]
    return func(word)

print(func('Xilinx'))

