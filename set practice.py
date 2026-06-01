# set1={1,2,3,4,5}
# set2={6,7,8,9,0}
# a=set1.union(set2)
# print(a)

# set3={3}
# print(set3)

# list=[4]
# print(list)

# tuple=(4,)
# print(tuple)
# tuple1=(4,5,6,7,8)
# print(tuple1)


# # sample_set={1,2,3,4,5,6,9.8,True,[1,2,3]}
# # print(type(sample_set))
# # print(sample_set)

# sample=[1,2,3,4,5,6,{1,2,3}]
# print(sample)

# tuple=(1,2,3,4,5,6,[1,2,3])
# print(tuple)
# tuple1=(1,2,3,4,{1,2,3})
# print(tuple1)

# sampl={1,2,3,4,5,(1,2,3)}
# print(sampl)

# # sample_set={1,2,3,4,5,6,9.8,True,{1,2,3}}
# # print(type(sample_set))
# # print(sample_set)


# number=set({100,200,300})
# print(number)


# strings=set('Quest')
# print(strings)

# string1=[10,20,30,40,'quest',(100,200,300)]
# print(string1)



# sample_sets={1,2,3,5,6,78,(1,2,3)}
# # print(sample_sets[3])

# for index,value in enumerate(sample_sets):
#     print(index,value)

# print(enumerate('quest'))


# person={'yaseen','shabin','mishal'}
# print(dir(person))

# person.add('hai')
# print(person)

# # person.add(tuple('hello'))
# # print(person)


# list1=["quest","clt"]
# for i in list1:
#     print(i)

# person.remove('yaseen')
# print(person)


# person.pop()
# print(person)


# person.discard('sree')
# print(person)

# person.discard('mishal')
# print(person)


# # subjects={'chemistry','biology','mathematics','social science'}
# # subjects.discard()

# set1={1,2,3,4,5,6,7,8,9,10,11}
# set2={12,13,15,17,19}
# set3={20,21,22}

# set4={100,200}
# a= set1 | set2 | set3
# print(a)

# print(set1.union(set2,set3,set4))

# set5={1,2,3,4,5}
# set6={2,3,4,8,9}
# print(set6.intersection(set5))

# set6.intersection_update(set5)
# print(set6)

# print(set5)
# print(set6)
# set5.intersection_update(set6)
# print(set5)

# set3={2,3,4,6,8}
# set4={2,3,1,2,3}
# print(set3.symmetric_difference(set4))

# numbers={i**2 for i in range(6)}
# print(numbers)

# numb={0,1,2,3,4,5,6,7,8,9}
# multiple_of_3={i for i in numb if i%3==0}
# print(multiple_of_3)

# even_or_odd={'even' if i%2==0 else 'odd' for i in numb}
# print(even_or_odd)

# check_num={0 if i<5 else 1 for i in numb}
# print(check_num)


# check={0 if i<5 else 1 if i>5 else 5 for i in numb}
# print(check)



# s=set()
# s.update({10,20,30})
# print(s)


# # a={i for i in range(6)}
# # search=int(input("Enter a number: "))
# # for i in range(len(a)):
# #     if search in a:
# #         print("The element exists")
# #     else:
# #         print("The elemnet doesnt exiats")



# # set3={1,2,3,4,5,6}
# # search = int(input("Enter the number to search:"))


# # for i in range(len(set3)):
# #   if search in set3:
# #    print("The element exist in set")
   
# # else:
# #     print("The element does not exist in set")


# set3={1,2,3,4,5,6}
# count=0
# for i in set3:
#    count+=1
# print(count)


# set3.update({10,20,30})
# print(set3)


# a={1,2,3,4,5}
# b=set()
# b=a.copy()
# print(b)



a=[10,20,30,40]
b=[]
for i in range(1,len(a)):
    b.append(a[i])
b.append(a[0])
print(b)


nums=[10,20,10,30,40,20,50,30]
dupl