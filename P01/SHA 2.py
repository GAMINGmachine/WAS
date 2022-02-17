'''import hashlib
def encrypt_string(hash_string):
    sha_signature = 1
    hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
hash_string = 'confidential data'
sha_signature = encrypt_string(hash_string)
print(sha_signature)
'''
import hashlib
m = hashlib.sha256()
m.update(b'confidential data')
print(m.hexdigest())
