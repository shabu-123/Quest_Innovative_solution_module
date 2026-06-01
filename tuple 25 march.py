t1=(1,2,3,4,5,78)
print(t1)
print(type(t1))

print(len(t1))
print(t1[0])





## list unpacking

sample_list=['apple','cherry','grapes','oranges'] ## list unpacking
*x,y,z=sample_list
print(x)
print(y)
print(z)

## tuple unpacking

person=('rami','shabu','imma','pappa')
p1,p2,p3,p4=person
print(p1)
print(p2)
print(p3)
print(p4)

person=('rami','shabu','imma','pappa')
p1,*p2,p3=person
print(p1)
print(p2)
print(p3)


person=('rami','shabu','imma','pappa')
person=(*person,'niyas','azeez')
print(person)

# del person
# print(person)

print(person[1])
print(person[1:])


print(person)
for p in person:
    print(p)

# for p in range(person):
#     print(p)

for p in range(len(person)):
    print(p)

for p in range(len(person)):
    print(person[p])



i=0
while i<len(person):
    print(person[i])
    i+=1

print(person)
print(person.count('pappa'))
print(person.count('idhh'))
print(person.index('shabu'))
# print(person.index('hhdh'))

pers=('shabu','shabin','rami','dhh')
pers+('sha','jdjd')
print(pers)

pers+=('sha','dhdhhd')
print(pers)



## tuples practical questions
