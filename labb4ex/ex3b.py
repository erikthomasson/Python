# paths = '/home/erik/Python/labb4ex'
# import os
# def mappar(path, lista=[]):
#     os.path.abspath(path)
#     print(path+ '\n')
    
#     for items in os.listdir(path):
#         currPath = f'{path}/{items}'
#         if os.path.isdir(os.path.abspath(currPath)):
#             print(f'{os.path.abspath(currPath)},dir')
#             mappar(currPath)
#         elif os.path.isfile(os.path.abspath(currPath)):
#             print(f'{os.path.abspath(currPath)},fil')
#             lista.append(os.path.abspath(currPath))
            
#     return lista

# print(mappar(paths))

import os
import hashlib
def mappar(path, lista=[]):
    os.path.abspath(path)
    print(path+ '\n')
    
    for items in os.listdir(path):
        currPath = f'{path}/{items}'
        if os.path.isdir(os.path.abspath(currPath)):
            print(f'{os.path.abspath(currPath)},dir')
            mappar(currPath)
        elif os.path.isfile(os.path.abspath(currPath)):
            print(f'{os.path.abspath(currPath)},fil')
            lista.append(os.path.abspath(currPath))
            
    return lista



path= input('Which map do you want to hash or check: ')
path = '/home/erik/Python/labb4ex'

files= mappar(path)
print(files)