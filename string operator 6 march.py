# encoding and decoding

string='mohamedshabin'
print(string.encode())

print(string.encode(encoding="utf-8"))
print(string.encode(encoding="utf-8", errors="strict"))

encoded_string=string.encode()
decoded_string=encoded_string.decode()
print(decoded_string)

# miscellanous

print("hello\tpython")
print("hello\tpython".expandtabs())
print("hello\tpython".expandtabs(4))
print("hello\tpython".expandtabs(12))
print("hello\tpython".expandtabs(16))
print("hello\tpython".expandtabs(20))
print("hello\tpython".expandtabs(25))
print("hello\tpython".expandtabs(51))
print("hello\tpython".expandtabs(100))

s="hello\tpython".expandtabs(20)
print(len(s))

print("sayana".translate({97:'x'}))
print(chr(108))
print("hello world".translate({108:'❤️'}))

print("hello world".translate({108:'y',111:'❤️'}))

text='xxxxxxxxyyyyyyyyzzzzzzz'
table=text.maketrans('x','z')
print(text.translate(table))

text='xxxxxxxxxxxyyyyyyyyyzzz'
table1=text.maketrans('x','z','y')
print(text.translate(table1))

r='shabin'
te=r.maketrans('sh','hs','i')
print(r.translate(te))
