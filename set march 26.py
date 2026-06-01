sample_set={ }
print(type(sample_set))

sample={1,2,3,4,5,8.7,'strings','quest'}
print(type(sample))
print(sample)


sample1={1,2,3,4,5,6,8.8,'strings','strings',1,2}
print(type(sample1))
print(sample1)

# sample_set={1,2,3,4,5,6,9.8,True,[1,2,3]}
# print(type(sample_set))
# print(sample_set)

sample_set={1,2,3,4,5,6,9.8,True,(1,2,3)}
print(type(sample_set))
print(sample_set)

# sample_set={1,2,3,4,5,6,9.8,True,{1,2,3}}
# print(type(sample_set))
# print(sample_set)


numbers=set({100,200,300})
print(numbers)

# number1=set(100,250,300)
# print(number1)

strings=set('Quest')
print(strings)


string1=[10,20,30,40,'quest',(100,200,300)]
print(string1)

strin2=(10,20,30,40,'quest',[1,2,3])
print(strin2)

# string3={1,2,3,4,5,[1,2,3]}
# print(string3)

strin3={1,2,3,5,6,(2,4,6)}
print(strin3)

sample_sets={1,2,3,5,6,78,(1,2,3)}
# print(sample_sets[3])

for index,value in enumerate(sample_sets):
    print(index,value)

print(enumerate('quest'))
print(list(enumerate('quest')))



## adding elements in a set

person={'yaseen','shabin','mishal'}
print(dir(person))

person.add('imma')
print(person)

# person.add({'hai'})
# print(person)

person.add(('shabu'))
print(person)

person.add(tuple('hello'))
print(person)


# list1=["quest","clt"]
# for i in list1:
#     print(i)

person.add('sha')
print(person)

# print(person)
# person+=('sha','ddf','ddff','ruruur')
# print(person)

# person+={'sha','dhdh'}
# print(person)

# person+=[1,2,3,4]
# print(person)

person.remove('shabu')
print(person)

person.pop()
print(person)

# person.dicard('sree')
# print(person)
subjects={'chemistry','biology','mathematics','social science'}
subjects.remove('chemistry')
print(subjects)

subjects.discard()