# def greet():
#     print("Hello welcome programmers....")

# # print(type(greet))
# greet()

# def greet(name):      ## here name indicates parameter
#     print(f"Hello welcome {name}")

# greet('shabin')   ## here shabin indicates arguments
# greet('shalu')


# def greet(m,n,o):
#     print(f"hello welcome {m}{n}{o}")

# greet("shbin",'shalu','sjs')


# def add(n1,n2):

#     print(n1+n2)
# add(17,18)



# # def add(n1,n2):
# #     return n1+n2
# # add(16,15)


# def add(n1,n2):
#     return n1+n2

# result=add(17,19)
# print(result)


# def eligibilty(age):
#     if age>28:
#         return "eligible"
#     else:
#         return "not eligible"
# r=eligibilty(25)
# print(r)


# def to_upper(string):
#     return string.upper()

# result=to_upper("shabin")
# print(result)

# ## type hinting

# def to_upper(s:str) -> str:
#     """this function converts the strings to upper case"""
#     return s.upper()

# print(to_upper("sreeraj"))

# positional arguments

def details(name : str, age : int, phone: list) -> str:
    """this function is user to collect details from user"""
    print(name)
    print(age)

result=details(25,'sreeraj', [55555555,77886666])
print(result)



### keyword arguments

# def details(name : str, age : int, phone: list) -> str:
#     """this function is user to collect details from user"""
#     print(name)
#     print(age)
#     print(phone)
# details(age=25,name='sreeraj', phone=[55555555,77886666])





# def add(a,b,c):
#     return a+b+c

# print(add(5,6,7))

# ## default arguments
# # def add(a,b,c):
# #     return a+b+c          ## this can be issued using default arguments

# # print(add(5,6))


# def add(a,b,c=9):
#     return a+b+c

# print(add(7,5))


# def add(a,b,c=9):
#     return a+b+c

# print(add(7,5,8))

# def add(a=2,b=5,c=8):
#     return a+b+c

# print(add(2,2,2))








