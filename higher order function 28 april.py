## reduce()
from functools import reduce

numbers=[1,2,3,4,5,6,7,8]
result=reduce(lambda x,y:x+y,numbers)
print(result)


string=["Hello"," ","world"]
result1=reduce(lambda x,y:x+y,string)
print(result1)

list=[1,2,34,6,7,9]
result2=reduce(lambda x,y: x if x>y else y,list)
print(result2)



min=reduce(lambda x,y: x if x<y else y,list)
print(min)

string=['Shabin','misha','lena']
result3=reduce(lambda x,y: x if len(x)>len(y) else y,string)
print(result3)

## remove duplicates from a list of numbers
list_num=[1,22,2,2,3,5,4,3,7,8,7]
result4=reduce(lambda x,y: x +[y] if y not in x else x, list_num, [])
print(result4)



### decorators

## original code no change but in behaviour changes are there

def my_decor(func):
    def wrapper():
        print("Function Execution Started")
        func()
        print("Function Execution Stopped")
    return wrapper

@my_decor
def greet():
    print("Hello Welcome......")

greet()


def To_upper(najad_function):
    def modify(*args):
        print("najad function execution started")
        result=najad_function(*args).upper()
        print("Successfully converted to upper case")
        return result
    return modify


@To_upper
def strings(s):
    return s

print(strings("My name is najad and iam python developer"))

