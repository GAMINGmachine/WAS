import hashlib
result = hashlib.md5(b'Web Application Security')
print("The byte equivalent of hash is:", end=" ")
print(result.digest())
