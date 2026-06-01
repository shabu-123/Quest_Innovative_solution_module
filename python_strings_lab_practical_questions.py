"""Beginner Level"""
""" 1. Create a string and print it."""
# string="Hello World"
# print(string)
"""2. Print each character of a string using indexing."""

str="shabin"
string_length=len(str)
for i in range(string_length):
    print(str[i])

"""3.Print the first and last character of a string."""
print(str[0])
print(str[-1])

"""4. Demonstrate positive and negative indexing on a string."""
print(str[1])
print(str[-1])

"""5. Extract the first five characters from a string using slicing."""
print(str[0:5])
"""6. Reverse a string using slicing."""
print(str[::-1])
"""7. Count the length of a string without using len()."""
count=0
for i in str:
    count+=1
print(count)
"""8. Convert a string to uppercase and lowercase."""
print(str.upper())
print(str.lower())
"""9. Capitalize the first letter of a string."""
print(str.capitalize())
"""10. Swap the case of each character in a string."""
print(str.swapcase())
"""11. Check whether a string starts with a specific substring."""
print(str.startswith("sha"))
"""12. Check whether a string ends with a specific substring."""
print(str.endswith("bin"))
"""13. Count the number of occurrences of a character in a string."""
print(str.count("a"))
"""14. Replace a word in a string with another word."""
print(str.replace("shabin", "shab"))
"""15. Remove leading and trailing spaces from a string."""
str_with_spaces="  shabin  "
print(str_with_spaces.strip())


"""Intermediate Level"""

"""1. Check whether a string contains only alphabets."""
print(str.isalpha())
"""2. Check whether a string contains only digits."""
print(str.isdigit())
"""3.Check whether a string is alphanumeric."""
print(str.isalnum())
"""4.Split a sentence into words using split()."""
sentence="My name is shabin"
print(sentence.split())
"""5.Join a list of words into a single string."""

words=["My", "name", "is", "shabin"]
joined_words=" ".join(words)
print(joined_words)
"""6. Find the first occurrence of a substring in a string."""
print(str.find("s"))
"""7. Find the last occurrence of a substring in a string."""
print(str.rfind("n"))
"""8. Remove a prefix from a string."""
print(str.removeprefix("sha"))
"""9. Remove a suffix from a string."""
print(str.removesuffix("bin"))
"""10. Center align a string within a given width."""
print(str.center(20))
"""11. Left justify and right justify a string."""
print(str.ljust(20))
print(str.rjust(20))
"""12. Pad a number string with zeros using zfill()."""
s='mishal'
print(s.zfill(9))
"""13. Use format() method in string formatting."""
name="shabin"
age=25
print("My name is {} and I am {} years old.".format(name, age))
"""14. Create a formatted string using f-strings."""
print(f"My name is {name} and I am {age} years old.")
"""15. Use partition() to split a string into three parts."""
print(str.partition("a"))


"""Logical Problem Solving"""
"""9. Remove all spaces from a string."""
print(str.strip())
"""12.Count the number of words in a sentence."""
sentence="My name is shabin"
print(sentence.count("a"))
"""14. Check whether a string contains special characters."""
strin='Shabin@123.-'
print(strin.isalnum())
"""15. Find the ASCII value of each character."""
for i in str:
    print("ASCII value of ",i,"is",ord(i))



    