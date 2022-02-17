import hashlib
with open ("Sample.txt", "rb") as f:
    bytes = f.read()
    print("Bytes read from a file:", bytes)
    result = hashlib.md5(bytes)
    print("Hash value:", result.digest())
    print("Hexadecimal value:", result.hexdigest())
    