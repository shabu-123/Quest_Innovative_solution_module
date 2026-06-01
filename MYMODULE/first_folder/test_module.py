from functools import reduce

list2=[10,20,30,40,50]
result=reduce(lambda x,y: x+y,list2)
print(result)


def greet(name):
    return f"Welcome {name}"


