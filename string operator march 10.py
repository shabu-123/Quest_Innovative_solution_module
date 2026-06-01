## swapcase
a="Quest"
b="calicut"
a,b=b,a
print(a)
print(b)

## palindrome

s="malayalam"
print(s[::-1])

q="mouse"
print(q[::-1])

if s == s[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")

## check if two strings are anagram
string1="listen"
string1sort=sorted(string1.lower())
print(string1sort)
string2="silent"
string2sort=sorted(string2.lower())
print(string2sort)
if string1sort == string2sort:
    print("The two strings are anagrams")
else:
    print("The two strings are not anagrams")


str1="aaabb"
str2="bbbaa"
str1sort=sorted(str1)
str2sort=sorted(str2)
if str1sort==str2sort:
    print("it is anagram")
else:
    print("it si not anagram")



# check frequency of each word

# s="Hello world"
# count=0
# for i in s:
#     count+=1
#     print(count)

s="hello world"

for i in range(len(s)):
    count=0
    print(s[i])
    for j in range(len(s)):
        if s[i]==s[j]:
            count+=1
    print(s[i],":",count)
    


    ## or

from collections import Counter
print(Counter(s))


## check first repeating character
s="programming"
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            print("the first repeating char is :",s[i])
            break
    else:
        continue
    break
    

# ## check first non repeating character

s="programming"
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if count(s[i])==count(s[j]):



###3. Remove duplicate characters from a string.

string="Hello shabin"
for i in range(len(string)):
    for 
