s="python"
print(s.center(25,"*"))

print(s.ljust(25))
print(s.ljust(25,"-"))

print(s.rjust(25))
print(s.rjust(25,"*"))

z="shabin"
print(z.isascii())

d='mishal123'
print(d.isascii())
h="dhdhsh@132"
print(h.isascii())

f="dhfhfh❤️❤️"
print(f.isascii())

print(s.zfill(10))

name="imma"
age=25
print("My name is {} and iam {} years old".format(name,age))

beauty='hdhdh'
ag=34
print("My name is {beauty} and iam {ag}years old")

name="imma"
age=25
print("My name is {} and iam {} years old".format(age,name))

name="imma"
age=25
print("My name is {1} and iam {0} years old".format(age,name))


print("My name is {:>10} and iam {} years old".format(name,age))

print("My name is {:<10} and iam {} years old".format(name,age))

print("My name is {:^} and iam {} years old".format(name,age))

print("My name is {:^} and iam {:05} years old".format(name,age))

print("My name is {:^10} and iam {} years old".format(name,age))

print(f"My name is {name} and iam {age} years old ")

print("my name is shabin \n and iam from mpm")    ## \n = escape sequence

print("'my name is shabin \n and iam from eut'")
print("'my name is shabin and iam'")

c= "welcome to the world of python"
print(c.split())

f="welcome-to-the-world-of-python"
print(f.split())

print(f.split("-"))
print(c.split("l"))

print(f.split("-",3))

print(c.rsplit(" ",3))
print(f.rsplit("-",3))

splitted=c.split()
print(splitted)
joined_string=" ".join(splitted)
print(joined_string)

join_str="-".join(splitted)
print(join_str)

g="job=python"
print(g.partition("="))

j="job=par=pyth"
print(j.partition("="))

y="python"
print(y.partition("python"))

r="my name is shabin"
print(r.partition(" "))
print(r.rpartition(" "))