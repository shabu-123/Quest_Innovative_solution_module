def square(a):
    return a**2
result=square(5)
print(result)

sq=lambda a: a**2
print(sq(5))

total=lambda a,b,c:a+b+c
result=total(5,3,8)
print(result)

even_odd=lambda x:x**2 if x%2==0 else x**3 
print(even_odd(5))

string_length=lambda x:len(x)
result=string_length('shabin')
print(result)

greater_num_2=lambda a,b: a if a>b else b
print(greater_num_2(5,6))

greater_num_3=lambda a,b,c:a if a>b and a>c else b if b>a and b>c else c
print(greater_num_3(5,3,4))

greater_num_3=lambda a,b,c:a if a>b and a>c else (b if b>a and b>c else c)
print(greater_num_3(5,3,4))

greater_or_equal=lambda a,b: a if a>b else b if b>a else "both are equal"
print(greater_or_equal(255,360))


## give one number check whether it is a multiple of 5 or multiple of 3 or multiple of both 3 and 5

multiple_num=lambda a: f"multiple of 3" if a%3==0 and not a%5==0else( f"multiple of 5" if a%5==0 else f"multiple of both 3 and 5")
print(multiple_num(15))