
def encrypt(msg, key):
    alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    encryptmsg=''
    index=0
    while len(msg) != len(encryptmsg):
        count=0
        for bokstav in alfabet:
            if msg[index] == bokstav:
                encryptmsg += str(alfabet[(count + key) % 26])            
                
            elif msg[index] == bokstav.lower():
                encryptmsg += str(alfabet[(count + key) % 26].lower())
            count +=1
        if len(encryptmsg) != index +1:
            encryptmsg += msg[index]
        index += 1   
    return encryptmsg


def decrypt(msg, key):
    alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    decryptmsg= ''
    index=0
    while len(msg) != len(decryptmsg):
        count=0
        for bokstav in alfabet:    
            if msg[index] == bokstav:
                decryptmsg += str(alfabet[(count - key) % 26])            
            elif msg[index] == bokstav.lower():
                decryptmsg += str(alfabet[(count - key) % 26].lower())
            count +=1
        if len(decryptmsg) != index +1:
            decryptmsg += msg[index]
        index +=1   
    return decryptmsg
