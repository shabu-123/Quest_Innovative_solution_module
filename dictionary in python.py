d={}
print(type(d))


dict={'name': 'shabin','Age': 22,'place': 'kalikavu','qualification':'PG'}
print(dict)

dict1={'name': 'shabin','Age': 22,'place': 'kalikavu','qualification':'PG','name': 'richu'}    ## duplicate values not allowed
print(dict1)

sample_list={1:'a',2: 'b',3:'a'}
print(sample_list)
sample_list1={1:'a',2:'b',3:'a',4.5:'d'}
print(sample_list1)

sample_dict={1:'a',2:'b',3:'a',4.5:'d',(1,2,3): 'tuple'}
print(sample_dict)
# sample_dict={1:'a',2:'b',3:'a',4.5:'d',{1,2,3}: 'set'}
# print(sample_dict)
# sample_dict={1:'a',2:'b',3:'a',4.5:'d',[1,2,3]: 'list'}
# print(sample_dict)
# sample_dict={1:'a',2:'b',3:'a',4.5:'d',{'name':'shabu','age':24}: 'dict'}
# print(sample_dict)

student1={'name':'shabu','age':24,'place': 'kkv'}
print(len(student1))

student1['place']='calicut'
print(student1)

student1['qualification']='pg'
print(student1)

print(student1['name'])
student1.update({'rollno': 46,'domain':'python'})
print(student1)
print(student1['rollno'])
print(student1.get('name','key doesn\'t exit'))


print(student1.get('teacher','key doesn\'t exit'))
print(student1.get('key doesn\'t exit'))

student1.update({'name':'sha','age':30})
print(student1)

# del student1
# del student1['place']
# del student1
# print(student1)
del student1['name']
print(student1)
p=student1.pop('place')    ## remove and return
print(p)
print(student1)

student1.popitem()  ## last index value is removed using popitem()
print(student1)
student1.popitem()
print(student1)

student1.clear()
print(student1)


student1 = {'name': 'shabu','age': 27,'batch':'fullstack'}

for i in student1:
    print(i)
# for key,value in student1:
#     print(i)
for key,value in student1.items():
    print(key,value)

for key in student1.keys():
    print(key)

for value in student1.values():
    print(value)

print(student1.items())
print(student1.keys())
print(student1.values())
