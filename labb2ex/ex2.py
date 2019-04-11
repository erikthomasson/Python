def count_e(word):
    e=0
    for letter in word:
        if letter == 'e':
            e += 1
    print(e)

# ex 2.3

def count_char(string, char):
    antal = 0
    for letter in string:
        if letter == char:
            antal +=1
    print(antal)

