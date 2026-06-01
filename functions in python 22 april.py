def add(a,b):
    return a+b
result=add(1,2)
print(result)

## arbitrary arguments

def add(*args):
    total=0
    for i in args:
        total+=i          ## it will be in tuple format
    return total

print(add(25,25))
print(add(24,56,75,45,677,45))
print(add(87))

## keyword arbitrary arguments

def details(**kwargs):
    print(kwargs)
    
details(name='sreeraj',age=25)
details(name='sreeraj',age=25, place='ktm')
details(name='sreeraj',age=25,place='ktm',phone=88778999)    #### it will be in dictionary format


def filtering(*args):
    for i in args:
        if i%2==0:
            print(i)

filtering(2,3,5,6,7,8,10,12,16)



def filtering(*args,**kwargs):
    print(kwargs)
    for i in args:
        if i%2==0:
            print(i)

filtering(2,3,5,6,7,8,10,12,16,name='sree')
