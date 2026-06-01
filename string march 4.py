# validation and checking

s='shabi'
print(s.isalpha())

s='12345'
print(s.isdigit())

z='sffg123'
print(z.isalnum())

q=""
print(q.isspace())
d= " "
print(d.isspace())

g="134566677"
print(g.isdecimal())

j='123444444.00'
print(j.isdecimal())

v="Quest Innovative Solution"
print(v.isupper())
print(v.islower())
print(v.istitle())
print(v.startswith('Q'))
print(v.startswith("q"))

y="mohamedshabin344@gmail.com"
print(y.endswith("@gmail.com"))

a="s"
print(a.isascii())

b='**2'
print(b.isascii())

# 4. Modification and Replacement

s="Python Django"
updated=s.replace("D","s")
print(updated)

s="python developer"
print(s.replace("developer","software"))

x="python develop develop develop"
print(x.replace("develop", "omg"))

x="python develop develop develop"
print(x.replace("develop", "omg", 2))

string="      Python Django"
print(string)
print(string.strip())

str="--------------udhddb shshdh"
print(str.strip("-"))

stri="1sdfgghhdff"
print(stri.strip("1"))

strin="abaaaaaaaaaaaaaaPython Djangoaaaaaaaaaaaaaaa"
print(strin.strip("ab"))

hdh="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Python Djangooooooooooooooooooooooooooo"
print(hdh.lstrip("@"))

dvf="dfgjjjjggggPython Dajtgn@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print(dvf.rstrip("@"))

name="Mr.Shoni"
print(name.removeprefix("Mr."))

print(name.lstrip("Mr."))


gend="Mr. Mr. Mr. Shoni"
print(gend.removeprefix("Mr."))
print(gend.lstrip("Mr."))
print(gend.removesuffix("ni"))












