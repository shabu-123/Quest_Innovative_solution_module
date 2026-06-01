"""operators"""

# numbers=[1,2,3,4,5,6,7,8,9]
# numbers+=10
# print(numbers)

## assignment operator

numbers=[1,2,3,4,5,6,7,8,9]
numbers+= [10]
print(numbers)

num=[1,2,3,4,5,6,7,8,9]
num+='10'
print(num)

num+='shabin'
print(num)

number=[1,2,3,4,5,6,7,8]
update_num=[10,20,35,46]
updated_numbers=number+update_num
print(updated_numbers)

test_list=number*10
print(test_list)

list1=[0]
list1*=10
print(list1)

nu=[1,2,3,4,5,6,7]
nu[2]=200
print(nu)

numb=[1,2,3,4,5,67]
numb[3]+=65
print(numb)

numb[3]*=400
print(numb)

numb[3]*200
print(numb)



value=[2,4,6,8,10,12,14]
print(100 in value)

values=[1,2,3,4,5,6,7,8,[10,20,30]]
print(30 in values)

print(30 in values[-1])
print(len(values[-1]))

## we have used here addition, repetition, membership operator and assignment operators(+=, *=,=)

## indexing

values=[1,2,3,4,5,6,7,8,[10,20,30]]
print(values[6])
print(values[7])
print(values[8])
# print(values[9])

print(values[-5])
print(values[-1][-1])
print(values[-1][2])
## indexing

# test=[1,2,3,4,5,6,7,8,9,[10,20,30],[100,200,300,[400,500,600],700,800,900]]
# print(test[10][6][0])

tests=[1,2,3,4,5,'quest','najad','richu',6,7,8,9,[10,20,30],[100,200,300,[400,500,600],700,800,900]]
print(tests[7][1])

## slicing

numbers=[1,2,3,4,5,'quest','najad','richu',6,7,8,9,[10,20,30]]
print(numbers[5:8])

print(numbers[::2])
print(numbers[::3])
print(numbers[::4])
print(numbers[:-1])
print(numbers[-8:-1])
print(numbers[-1:7:-1])
print(numbers[6][1:4])

matrix=[[0,1,2],[3,4,5],[6,7,8]]
print(matrix)
print(len(matrix))
for matrices in matrix:
    

 

 for m in matrices:
   print(m)


