### Section 1: Beginner Level

### 1. Create a list of five integers and print all elements using a for loop.
list1=[1,2,3,4,5]
new_list=[i for i in list1 if i in list1]
print(new_list)

# for i in range(5):
#     print(list1[i]))

### 2. Write a program to find the length of a list without using len().
list_value=[1,2,3,4,5]
count=0
for i in list_value:
    count+=1
print("Length of list: ", count)

### 3. Create a list of numbers and print the maximum and minimum values.

list1=[2,4,6,8,10]
print(max(list1))
print(min(list1))

### 4. Write a program to append a new element to a list entered by the user.
# list2=[10,20,30,40,50,60,70,80,90]
# new_element=int(input("Enter a number: "))
# list2.append(new_element)
# print(list2)

### 5. Insert an element at a specific position in a list.
list1.insert(7,-20)
print(list1)

### 6. Remove an element from a list using remove() and pop().
list1.remove(8)
print(list1)
list1.pop()
print(list1)
list1.pop(0)
print(list1)

### 8. Reverse a list without using reverse().
list3=[10,20,30,40,50]
print(list3[::-1])
###9. Sort a list of numbers in ascending and descending order.
sort_num=[1,2,3,54,5,6,78]
sort_num.sort()
print(sort_num)
sort_num.sort(reverse=True)
print(sort_num)
### 10. Create a list of numbers and print only the even numbers.
list2=[1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if i%2==0:
        print("The even numbers")



a=[1,2,3]
b=[4,5,6]
print(a+b)

fruits=["apple","banana","cherry"]
print("apple" in fruits)
    

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for item in row:
        print(item,end="")
    print()


squares = []
for i in range(1, 6):
 squares.append(i * i)
 print(squares)
 
