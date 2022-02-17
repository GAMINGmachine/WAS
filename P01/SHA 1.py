import hashlib
m = hashlib.sha1()
m.update(b'The quick brown fox jumps over a lazy dog')
print(m.hexdigest())
