def greet():
    print("Welcomew to djjf")
greet()

def display_name(name):
    print("Name:", name)
display_name("shabin")

def add(a,b):
    return a+b
result=add(5,6)
print(result)

def is_even(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
is_even(3)

def add(a,b):
    return a+b
print(add(6,7))


def square(n):
    return n**2
reuslt=square(3)
print(reuslt)


def is_even(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
result=is_even(8)
print(result)


def find_largest(a,b):
    if a>b:
        return a
    else:
        return b
result=find_largest(7,13)
print(result)




def is_even(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
result=is_even(7)
print(result)

def check_positive(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"
result=check_positive(6)
print(result)



# def multiply(a, b):
#     return a * b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Multiplication:", multiply(a, b))



def full_name(first, last):
    return first +  last

print(full_name("Mohamed", "Shabin"))


def count_vowel(text):
    vowels="aeiouAEIOU"
    count=0

    for char in text:
        if char in vowels:
            count+=1
        
    return count

print(count_vowel("python"))

def factorial(n):
    result=1

    for i in range(1,n+1):
        result *= i
    
    return result
print(factorial(6))



def sum_of_digits(num):
    
    return sum(numbers)
result=sum_of_digits(1234)
print(result)



