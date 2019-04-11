import os

paths = os.listdir('/home/erik/Python/labb4ex')
print(paths)
for item in os.listdir('/home/erik/Python/labb4ex'):
    print(item)


directory = "/home/erik/Python/labb4ex"
items = os.listdir(directory)
print(items[0])
for item in items:
    path = directory + '/' + item
    print(path, ', ' , os.path.isdir(path))