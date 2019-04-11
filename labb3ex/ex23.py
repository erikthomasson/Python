
def func(word):
    word=word.lower()
    if word == "":
        return True
    if word[0] == word[-1]:
        word= word[1:-1]
        return func(word)
    return False

print(func('Racecar'))
