import base64
string = "WAS is the best"
string_bytes = string.encode('ascii')
base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode('ascii')
print(f"encoded string : {base64_string}")
