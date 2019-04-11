
def count_vowels(string):
    count=0
    for letter in string:
        if letter == 'a' or string == 'e' or string == 'o' or string == 'i' or string == 'u':
            count += 1
    return count
