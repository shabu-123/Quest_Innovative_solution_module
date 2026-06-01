### higher order functions



###1. map()

### . map() is a function that applies do this function to every item

def square(nums :int) -> int:
    return nums**2

numbers=[2,3,4,5,6,7,8,9]
result=map(square,numbers)
print(result)


def square(nums :int) -> int:
    return nums**2

numbers=[2,3,4,5,6,7,8,9]
result=list(map(square,numbers))
print(result)

result1=list(map(lambda x: x**2,numbers))
print(result1)

numb=[2,7,5,15,20,6,8,25,8,0,5]
print(len(numb))
result2=list(map(lambda x:x%5==0,numb))
print(result2)
print(len(result2))



## in map we should give operation whereas in filter we should give condition
result3=list(filter(lambda x:x%5==0,numb))
print(result3)

string=["shabin","mishal","ramees","sakeena"]
result4=list(filter(lambda x: x in 'aeiou',str(string)))
print(result4)


# def vowels(string):
#     for string in 'aeiou':
#         if vowels in string:
#             return True
#         else:
#             return False

# string=['Shabin','mishal']
# result=vowels(string)
# print(result)


sample_list=[2,3,4,66,{},[]]
print(any(sample_list))
print(all(sample_list))

names=['shabin','najad','sss']
result5=list(filter(lambda x: any(ch in 'aeiouAEIOU' for ch in x),names))
print(result5)

email=['dhdhh@gmail.com','dhdhdgsf@gmail.com','hdggfghs@yahoo.com','sddhhdhsh.co.in']
# result6=list(filter(lambda x: any(ch.endswith('@gmail.com') for ch in email),email))
# print(result6)

res=list(filter(lambda x: any(x.endswith(d) for d in ["gmail.com","yahoo.com"]),email))
print(res)


## check multiple of 3 and then find cubes
numb=[1,2,3,4,6,9,12,15,21,76,46]
r=list(filter(lambda x: x%3==0,numb))
q=list(map(lambda x:x**3,r))
print(q)

## or

result=list(map(lambda x: x**3, filter(lambda y: y%3==0, numb)))
print(result)

### give some strings in length and string length is greater than 4 if that condition is true convert to upper case
