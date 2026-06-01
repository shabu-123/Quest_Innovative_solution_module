numbers=[]

for i in range(1,11):
    numbers.append(i)
print(numbers)

number=[i for i in range(1,11)]
print(number)

fruits=['apple','cherry','banana','kiwi','mango']
new_list=[x for x in fruits if 'a' in x]
print(new_list)

## to find square

square=[i**2 for i in range(1,11)]
print(square)

sq_cube=[]

for i in range(1,11):
    if i%2==0:
        sq_cube.append(i**2)
    else:
        sq_cube.append(i**3)
print(sq_cube)

sq_cubes=[i**2 if i%2==0 else i**3 for i in range(1,11)]
print(sq_cubes)
### using list comprehension make a string to upper character
s=['my','name','is','shabin']
upper_list=[i.upper() for i in s]
print(upper_list)

## append animal list and find length of each string using list comprehension

animal_list=['cat','dog','snake']
length=[len(i) for i in animal_list]
print(length)

## given a list if the string is starting vowel make it to upper case if it is consonant make it to title case
sh=['mary','sake','rashe','aishal']
string_list=[i.upper() if i[0] in 'AEIOUaeiou' else i.title() for i in sh]
print(string_list)

sha=['Shabin','Aeioijf','adhdh','ejjfj','Ejdjd','Ramees']
new_list=[]
for i in sha:
    if i[0] in 'AEIOUaeiou':
        new_list.append(i.upper())
    else:
        new_list.append(i.title())
print(new_list)

## extract positives from a list
list=[-1,-2,-3,-4,-5,0,1,2,3,4,5]
extract=[i for i in list if i>0 ]
print(extract)

## Extract vowels from a string or a sentence
string='programming'
extract_vowels=[i for i in string if i in 'AEIOUaeiou']
print(extract_vowels)

## find common elements from the two lists
list1=[1,2,3,4,5,6,7,8,9]
list2=[4,3,8,11,43,21,9]
common_list=[i for i in list1 if i in list2]
print(common_list)

## given a string with integers , convert to integers and store it in a new list

str_int=['1','2','3','4','5']
int_list=[int(i) for i in str_int ]
print(int_list)

# str_int=['1','2','3','4','5','sreeraj']
# int_list=[int(i) for i in str_int ]
# print(int_list)

str_int=['1','2','3','4','5','shabin']
int_list=[int(i) for i in str_int if i.isdigit() ]
print(int_list)








