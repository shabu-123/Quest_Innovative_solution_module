# age=-5

# if age<0:
#     raise ValueError('age cant be negative')


# mark=500
# if mark>200:
#     raise ValueError('mark should be less than or equal to 200')


## using try except method

# try:
#     mark=200
#     if mark>100:
#         raise ValueError("value must be less than or equal to 100")
# except Exception as e:
#     print(e)


# try:
#     mark=200
#     if mark>100:
#         raise ValueError("mark should be less than or eual to 100")
# except ValueError as e:
#     print(e)



# try:
#     mark="500"
#     if int(mark)>200:
#         pass
#     elif isinstance(mark,int):
#         raise TypeError("mark cant be string....")
# except ValueError as e:
#     print(e)



# class AgeError(Exception):
#     pass

# age=-5
# if age<0:
#     raise AgeError("Age cant be negative")



# class AgeError(Exception):
#     pass

# class VoteError(Exception):
#     pass

# age=-6

# if age<0:
#     raise AgeError("age cant be negative")







#Example 1

age = -5

if age<0:
    raise ValueError("Age cannot be negative")
print("Valid age")


num=int(input("Enter a positive number: "))

if num <=0 :
    raise ValueError("Number must be positive")

print("Square:",num*num)

name=input("Enter your name:")
if name == "":
    raise ValueError("Name cant be empty...")

print("Value inserted")



