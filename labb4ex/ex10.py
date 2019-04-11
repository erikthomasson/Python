siffror = [1,2,3,4,5,6,7,8,9,0]
bokstäver = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J',\
'j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u'\
,'V','v','W','w','X','x','Y','y','Z','z']
streck= ['-','_']
ordet = 'username@domain.ext'
def is_valid(address):
    #print(address.index('@'))
    #print(address.index('.'))
    try:
        username= address[:address.index('@')]
        domain = address[address.index('@')+1:address.index('.')]
        extension = address[address.index('.')+ 1:]
    except: 
        return False
    #print(username)
    #print(domain)
    #print(extension)

    for letter in username:
        if letter not in siffror + bokstäver + streck and username != '':
            return False
    for letter in domain:
        if letter not in bokstäver + siffror and domain != '':
            return False
    if len(extension) >3:
        return False
    return True

fil = open('emails.txt')
for lines in fil:
    if is_valid(lines.split()[0]):
        print(lines)
    




