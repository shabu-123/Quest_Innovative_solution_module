sample_list=[1,2,3,4,5,6,7,8,9,20,10,100]
print(dir(sample_list))
sample_list.append(3000)
print(sample_list)

sample_list.append('quest')
print(sample_list)

sample_list.append(3.9)
print(sample_list)

# sample_list.append(1,300)
# print(sample_list)

sample_list.insert(1,4000)
print(sample_list)

sample_list.pop()                   ## pop is used for removing element in the last index
print(sample_list)

sample_list.pop()
print(sample_list)


sample_list.pop(-2)             ## here -2 indicates index value   will remove the specified index value
print(sample_list)

# sample_list.remove()
# print(sample_list)

sample_list.remove(3)       ## here 3 indicates value
print(sample_list)


# sample_list.remove(100)
# print(sample_list)

# sample_list.clear()
# print(sample_list)

# sample_list.clear(1)
# print(sample_list)


print(sample_list.count(7))

print(sample_list.count(400))
# print(sample_list.count())

# print(sample_list.count(1,4))

print(sample_list)
copy_list=sample_list.copy()
print(copy_list)


sample_list1=[1,2,3,4,5,6,[7,8,9]]
copy_list1=sample_list1.copy()
print(copy_list1)
copy_list1[-1][-1]=900
print(copy_list1)
print(sample_list1)

print(sample_list)
sample_list.sort(reverse=True)
print(sample_list)
sample_list.sort()
print(sample_list)

a=['my','name','is','Mohamed','Shabin','aa','ABC']    ## on the basis of ascii value in a string we are sorting not on the basis of length
a.sort() 
print(a)

a=['my','name','is','Mohamed','Shabin','aa','ABC']    ## on the basis of ascii value and here length in a string we are sorting not on the basis of length
a.sort(key=len) 
print(a)


# a=['my','name','is','Mohamed','Shabin','aa','ABC',10]    ## on the basis of ascii value in a string we are sorting not on the basis of length
# a.sort() 
# print(a)

# a=['my','name','is','Mohamed','Shabin','aa','ABC',[10,20,30]]    ## on the basis of ascii value in a string we are sorting not on the basis of length
# a.sort() 
# print(a)


print(sample_list)
s=['MY','my','name','is','sreeraj']
sample_list.extend(s)
print(sample_list)

sample_list.extend("Quest Solutions")
print(sample_list)
print(s)

# sample_list.extend(10)
# print(sample(list))

sample_list.extend([10])
print(sample_list)

print(sample_list.index(6))

print(sample_list.index(7,0,6))    # syntax = value, start, 

sample_list.reverse()
print(sample_list)

sample_list2=[1,2,3,4,5,6,7,8,9]
print(len(sample_list2))

print(max(sample_list2))

print(min(sample_list2))

print(sum(sample_list2))

s=sorted(sample_list2)
print(s)
print(sample_list2)
s=sorted(sample_list2,reverse=True)
print(s)
print(sample_list2)

x=['MY','my','name','is','Mohamed','DShabin','AAA','x']
print(min(x))
print(max(x))
print(sorted(x))







s=[1,2,3,4,5,6,7,8,9]
s.sort()                  ## this will be an issue if there are duplicate values
print(list1)
print(list1[-2])

for i in range(len(list1)):
    print(list1[i])

    if list1[i]>large:      ## large =0 and list1_large=0

        list1_large=lis

