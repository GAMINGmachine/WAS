import html
a_string = "&lt body &gt"
decoded_string = html.unescape(a_string)
print(decoded_string)
