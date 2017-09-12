import hashlib

hash_object = hashlib.md5(b'Hi')
print(hash_object)
print(hash_object.hexdigest())
print(hash_object.digest())

# hexdigest returns a HEX string representing the hash, in case you need the sequence of bytes you should use digest instead.
# "b" preceding the string literal, this converts the string to bytes
