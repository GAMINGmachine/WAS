import urllib.parse
query = { "a" : "123", "b" : "256"}
encoded_query=urllib.parse.urlencode(query)
print(encoded_query)
