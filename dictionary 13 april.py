nested_dict={
'student1': {
    'name': 'shabin',
    'age': 34,
    'gender': 'male',
    'batch': 'full stack',
    'phone': [9999767655,476578384]
},
'student2': {
    'name':'yaseen0',
    'age': 32,
    'batch': 'data science'
}
}

print(nested_dict['student1']['batch'])
print(nested_dict['student1'])
print(nested_dict['student1']['phone'])
print(nested_dict['student1']['phone'][1])

nested_dict['student2']['phone']=[747473364784,4837266374]
print(nested_dict)

### dictionary comprehension

squared_dict={x:x**2 for x in range(1,11)}
print(squared_dict)

even_squared_number={x:x**2 for x in range(1,11) if x%2==0}
print(even_squared_number)

alphanum_dict={'a':1,'b':2,'c':3,'d':4}
filtered_dict={k:v for k,v in alphanum_dict.items() if v%2==0}
print(filtered_dict)

sample_dict={'a':1,'b': 4,'c':5,'d':8,'e':9}
final_dict={v:k for k,v in sample_dict.items()}
print(final_dict)

sample_dict=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
new_dict={x:ord(x) for x in sample_dict}
print(new_dict)

sample_di1=[1,2,3,4,5,6,7,8,9,10]
squared_number={k:k**2 if k%2==0 else k**3 for k in sample_di1}
print(squared_number)