'''Hasha filer eller checka filer på hashning av: Erik Thomasson'''
import os
import hashlib
def mappar(path, lista=[]):
    '''Returnerar en lista med alla filer under mappen som skrivs in som invärde i funktionen'''
    os.path.abspath(path)
    for items in os.listdir(path):
        currPath = f'{path}/{items}'
        fullpath = os.path.abspath(currPath)
        if os.path.isdir(fullpath):
            mappar(currPath)
        elif os.path.isfile(fullpath):
            lista.append(fullpath)
            
    return lista

path= input('Which map do you want to hash or check: ')
path = '/home/erik/Python/labb4ex'

files= mappar(path)
oldhashdfiles=[]
hashdfiles=[]
def hashthefile(abspathtofile):
    '''Hashar filen som sätts in som värde i funktionen'''
    with open(abspathtofile, 'rb') as fil:
        inside =fil.read()
        crypt = hashlib.md5(inside)
        return crypt.hexdigest()

diction={} # Dictionary file1:hash1, file2hash2, ...
for items in files:
    diction[items]= hashthefile(items)
def make_a_file():
    '''Making a file with the files names and its hashes'''
    hashfil=open('/home/erik/Python/labb4/filesanditshashes', 'w')
    for items in diction:
        hashfil.write(f'{items}\n{diction[items]}\n')

def check_the_file():
    '''Opens the file with the (files and its hashes) and compare it to the ("new files" and its hashes)'''
    oldfiles = []
    olddict= {}
    index = 0
    hashfile=open('/home/erik/Python/labb4/filesanditshashes')
    for lines in hashfile:
        oldfiles.extend(lines.split())
    for items in oldfiles:
        if index % 2 == 0:
            olddict[items]= oldfiles[index+1]
        index +=1
    changedfiles=[]
    newfiles=[]
    delfiles=[]
    index=0
    for keys in diction:
        if keys in olddict:
            if not diction[keys] == olddict[keys]:
                changedfiles.append(keys)
        else:
            newfiles.append(keys)
    for keys in olddict:
        if keys not in diction:
            delfiles.append(keys)

    print('These files are new:')
    for items in newfiles:
        print(f'{items}\n')

    print('These files has been removed:')
    for items in delfiles:
        print(f'{items}\n')
    
    print('These files has been changed:')
    for items in changedfiles:
        print(f'{items}\n')
    

if 'filesanditshashes' not in os.listdir('/home/erik/Python/labb4'):
    make_a_file()

else:
    check_the_file()