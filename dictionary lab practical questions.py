### --- PART 1: DICTIONARY BASICS & CREATION ---

### 1. Create a dictionary representing a 'Laptop' with keys: brand, model, and price.
dict1={'brand': 'inspiron', 'model': 'dell', 'price': 50000}
print(dict1)

### 2. Access the value of the 'model' key using square brackets.

print(dict1['model'])

### 3. Access the value of a key that doesn't exist using .get() and explain why it's safer than [].
print(dict1.get('brand','key doesnt exist'))
print(dict1.get('size','key doesnt exist'))
# print(dict1['size'])

### 4. Create an empty dictionary using both {} and the dict() constructor.
dic={}
print(dic)

dict2=dict()
print(dict2)

## 5. Add a new key-value pair 'processor': 'i7' to an existing dictionary.
dict1['processor']='i7'
print(dict1)

## 6. Update the 'price' of the laptop to a new value.
dict1['price']=60000
print(dict1)

### 7. Use the len() function to find how many key-value pairs are in a dictionary.
print(len(dict1))

### 8. Create a dictionary where the keys are numbers 1 to 5 and the values are their squares.
dict3={1: 1, 2: 4, 3: 9, 4 : 16, 5: 25}
print(dict3)

dict3={x: x**2 for x in range(1,6)}
print(dict3)

### 9. Check if a specific key exists in a dictionary using the 'in' operator.
print(6 in dict3)
print(5 in dict3)
print('model' in dict1)
# print(model in dict1)

## 10. Delete a key-value pair using the 'del' keyword and handle the case if the key is missing.
del dict1['model']
print(dict1)

### --- PART 2: METHODS & MANIPULATION ---
## 11. Use the pop() method to remove a key and store its value in a variable.
p=dict1.pop('price')
print(p)
### 12. Use popitem() to remove the last inserted item and explain its behavior in Python 3.7+.
print(dict1)
dict1.popitem()
print(dict1)
### 13. Use the keys() method to print all the keys in a dictionary.

dict4={'name': 'mohamed', 'age': 26, 'height': 168, 'qualification': 'pg'}
print(dict4.keys())

### 14. Use the values() method to print all the values in a dictionary.
print(dict4.values())
### 15. Use the items() method to iterate through a dictionary and print "Key: Value" for each pair.
print(dict4.items())
### 16. Merge two dictionaries: {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using the update() method.
dict4.update({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(dict4)