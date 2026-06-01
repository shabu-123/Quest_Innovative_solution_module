# # f=open("sample.txt")
# # print(f.read())
# # f.close()


# ## or

# with open("sample.txt") as f:          ## as = temporary name
#     print(f.read())

# with open("sample.txt", 'r') as f:     ## r=read
#     print(f.read())

# # with open("sample.txt", 'r') as f:     ## r=read
# #     print(f.read())
# #     f.write("fhfhdhfhfjgjgj")

# with open("sample.txt", 'w') as f:      ## w= write mode only will make changes to sample.txt file
#     f.write("have a great day")
#     f.write("Python Programmers")

# with open("sample.txt",'w') as f:      ## in this it will it will get kalikavu will not consider have a great day and python programmers will consider only a block of code
#     f.write("Kalikavu")

# # with open("sh.txt",'r') as f:
# #     pass

# with open("Sh.txt",'w') as f:
#     pass

# with open("sample.txt",'r+') as f:
#     f.write("shabin")
#     f.write("shabu")


# with open("sample.txt","r+") as f:            ## if we mention read before write the character will be displayed on right side.(last part).
#     f.read()
#     f.write('kalik')


# with open("sample.txt","r+") as f:
#     f.seek(0)
#     f.read()
#     f.write('kalik')

# with open("sample.txt","r+") as f:
#     f.seek(25)
#     f.read()
#     f.write('kalik')




    
## 04 may 2026

# with open("sample.txt",'w+') as file:
#     file.write("Quest Innovative Solutions")
#     file.write(", Calicut")
#     print(file.tell())
#     file.seek(0)
#     print(file.tell())
#     print(file.read(6))
    

# with open('sample.txt','a') as file:
#     print(file.tell())
#     file.seek(2)
#     file.write("Python full stack trainers")
#     print(file.tell())
#     file.seek(0)
#     print(file.read())


# with open('sample.txt','a+') as file:
#     print(file.tell())
#     file.seek(2)
#     file.write("Python full stack trainers")
#     print(file.tell())
#     file.seek(0)
#     print(file.read())

# with open("gh.txt","x+") as f:
#     f.write("This is exclusive creation file....")
#     f.write("Testing...")
#     print(f.read())

# with open("im.txt","a+") as f:
#     print(f.writable())
#     print(f.readable())
#     f.seek(0)
#     # print(f.read(20))
#     print(f.readline(20))

#     f.seek(0)
#     data=f.readlines(2)
#     print(data)


##05 may 2026

with open("sample.txt", "a+") as f:
    print(f.tell())
    f.seek(0)
    data=f.readlines()
    print(data)

# data[0]='Shabin'
# print(data)

data=set(data)

with open("write_example.txt","w+") as file:
    file.writelines(data)



## with , for and if else condition

with open("sample.txt","r+") as f:
    line=int(input("Enter the number of lines to read: "))
    for i in range(line):
        f.readline()


## close file

##used to close an opened file and free the resources associated with it.
syntax: file_object.close()










    





