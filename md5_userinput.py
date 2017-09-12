import hashlib

myString = input('Enter first string to hash: ')

hash_obj = hashlib.md5(myString.encode())

print(hash_obj.hexdigest())

