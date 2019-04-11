import hashlib
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())


fil =open('Alice.1.txt', 'rb')
inside= fil.read()
print(inside)
cryptfil= hashlib.sha1(inside)
print(cryptfil.hexdigest())
fil.close()