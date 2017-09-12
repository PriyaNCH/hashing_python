import hashlib

hash_obj = hashlib.sha1(b'Hello')

hex_obj = hash_obj.hexdigest()
print(hex_obj)