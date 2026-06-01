name="shabin"
print(type(name))
print(len(name))

numbers="112234567"
print(type(numbers))

emoji="❤️"
print(emoji)
print(type(emoji))

sequences="!@#$%^&*"
print(type(sequences))

company='quest innovative solution'      # for whitespaces we are counting length
print(len(company))

#numb=123
#print(len(numb))

# explicit = we are defining datatype of variable

num=133
print(len(str(num)))


name='shab'

for char in name:
    print(char)


name='mishal'
for char in name:
    print(char, end=" ")


print(ord("A"))      # asci value = whichever letter has low value we will take corresponding asci value
                     # to convert character to ascii value we use ordered function
print(ord('a'))
print(ord("B"))


print(chr(65))       # chr = character     
                     # to convert ascii to character we use chr function


white_space="          "
print(type(white_space))
print(len(white_space))


# indexing

s="Hello programming"
print(s[4])

print(s[-9])


# slicing

z="python data types"
print(z[1:4])

print(z[1:])
print(z[:6])
print(z[0:])
print(z[::])
print(z[::1])
print(z[::2])
print(z[-1:-5])
print(z[-5:-1])
print(z[-5:17])
print(z[-5:19])
print(z[-1:-5:-1])
print(z[::-1])

print(chr(96))