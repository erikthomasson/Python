age = int()
def introduce(name='unknown', age='secret'):
    if name != 'unknown' and age != 'secret':
        print("My name is", name + '. I am', age, "years old.")
    elif age == 'secret':
        print('My name is', name + '. My age is a secret.')
    elif name == 'unknown':
        print("My name is", name + '. I am', age, "years old.")
        
    
    
    # elif name:
    #     print('My name is', name + '. My age is a secret.')
    # else:
    #     print('My name is unknown. My age is a secret.')

