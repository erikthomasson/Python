word = 0
while word != 'quit':
    word = input('Write a word: ')
    index = 0
    if word == 'quit':
        print('Exiting ...')
        break
    for letter in word:
        
        index += 1
        if letter == word[-index]:
            continue
        if letter != word[-index]:
            print(word, 'is not a palindrom')
            break
    if index  == len(word):
        print(word, 'is a palindrom')
        break

word=0
while word != 'quit':
    word = input('Write a word: ')
    index =0
    if word == 'quit':
        print('Exiting ...')
        break
    for letter in word:
        if letter == word[::-index]:
            index += 1
            print(f'{word} is a palindrom')
        
        else: 
            print(f'{word} is not a palindrom')
    break    
    




