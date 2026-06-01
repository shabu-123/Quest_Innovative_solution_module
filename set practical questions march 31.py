### Section 1 – Basic Set Programs
### 1.Create a set containing 5 numbers and print the set.

set1={1,2,3,4,5}
print(set1)
### 2.Create a set with mixed data types and print each element.
# set2={2,3,'strings',True,4.6,[1,2,3]}   ## we cant add list because it is unhashable and it is mutable
# print(set2)
set2={2,3,'sterings',True,4.6,(1,2,3)}  ## tuple is working inside the set
print(set2)
# set2={2,3,{1,2,3}}   ## we cant add set inside the set
# print(set2)

### 3. Write a program to create a set from a list.
list1=[1,2,3,4,5,6,7,8,9,7]
print(list1)
print(set(list1))

### 4. Write a program to remove duplicate elements from a list using a set.
list2=[1,2,3,4,5,6,7,5,4,3,2]
print(set(list2))




### 5.Create an empty set and add three elements to it.
set2=set()
print(set2)
set2.add(1)
print(set2)
set2.add(2)
set2.add(3)
print(set2)
set2.update((1,2,3))
print(set2)

### 6. Write a program to check if an element exists in a set.

# set3={1,2,3,4,5,6}
# search = int(input("Enter the number to search:"))


# for i in range(len(set3)):
#   if search in set3:
#    print("The element exist in set")
   
# else:
#     print("The element does not exist in set")

### 7.Create a set and print all elements using a for loop.
set6={1,2,3,5,6,7,8}
new_set1={i for i in set6 if i in set6}
print(new_set1)

### 9.Write a program to convert a tuple into a set.

tuple=(1,2,3,4,5,6)
new_set=set(tuple)
print(new_set)

### 10. Write a program to convert a set into a list.
sets={2,4,6,8,10,12,14}
new_list=list(sets)
print(new_list)


### Section 2 – Adding and Removing Elements
### 11.Create a set and add a new element using add().
set1={1,2,3,4,5,6}
set1.add(7)
print(set1)

### 12.Write a program to add multiple elements to a set using update().
a={i for i in range(1,10) }
a.update("shabin",'mishal')
a.update({"shabin","mishal"})
print(a)

### 13.Write a program to remove an element using remove().

b={i for i in range(1,10)}
b.remove(1)
print(b)

### 14.Write a program to remove an element using discard().
c={i for i in range(2,8)}
c.discard(6)
print(c)
c.discard(12)
print(c)

### 15.Write a program to remove a random element using pop().
a={i for i in range(1,9)}
a.pop()
print(a)

### 16.Write a program to clear all elements from a set.
a=set()
a.clear()
print(a)

### 17.Write a program to copy a set into another set.
a={i for i in range(7,14)}
b=set()
b=a.copy()
print(b)
print(a)

### 18.Write a program to add elements from a list into a set.
a=[i for i in range(1,9)]
a.extend([10,20,30,40])
print(a)
b=set(a)
print(b)

### 19. Write a program to add elements from a tuple into a set.
a=(1,2,3,4,5,6,7,8,9,10)
b=set(a)
print(b)
b.update({'shabin','mishal'})
print(b)

### 20. Write a program to update a set with another set.

set1={1,2,3,4,5,6,7,8}
set2={2,45,8,7,6,9}
for i in set1:
 set2.update({i})
print(set2)

### Section 3 – Set Operations

### 21. Write a program to find the union of two sets.
a={i for i in range(2,10)}
b={i for i in range(3,9)}
new_set={i for i in a or b}
print(new_set)




### 




