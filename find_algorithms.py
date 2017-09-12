import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# The algorithms_available method lists all the algorithms available in the system, 
# including the ones available trough OpenSSl. In this case you may see duplicate names in the list. 
# algorithms_guaranteed only lists the algorithms present in the module. md5, sha1, sha224, sha256, sha384, sha512 are always present.