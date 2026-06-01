# b=[10,20,30,40,50,60,10]
# b.remove(10)
# print(b)
# b.pop(-2)
# print(b)


# # a=[1,2,3,4,5,6]
# # num=int(input("Enter a number: "))
# # for i in a:
# #     if i in a:
# #         print("The element exists in a list")
# #     else:
# #         print("The element doesnt exists in a list")
# #     break

# # list=[1,2,3,4,5]
# # num=int(input("Enter a number: "))
# # if num in list:
# #         print("The element exist")
# # else:
# #         print("not exist")



# list=[1,2,3,4,5]
# list.sort()
# print("Ascending:",list)

# list


# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i % 2==0:
#         print(i)



# a=[1,2]
# b=[3,4]
# c=a+b
# print(c)

# # a=[10,10,20,30,40,30,100]
# # new_list=list(set(a))
# # print(new_list)

# # lst = [1, 2, 2, 3, 4, 4]
# # unique = list(set(lst))

# # print(unique)


# lst=[1,2,2,3,4,4,5]

# unique_list=[]

# for i in lst:
#     if i not in unique_list:
#         unique_list.append(i)

# print(unique_list)


# # lis=[10,11,12,1,3,4,8,10,11,12]
# # a=set(lis)
# # print(a)
# # b=list(a)
# # print(b)



# lst = [[1, 2], [3, 4], [5]]

# flat = []
# for sub in lst:
#     for i in sub:
#         flat.append(i)

# print(flat)




list=[[10,20],[30,40],[50,60]]
flat=[]
for sub in list:
    for i in sub:
        flat.append(i)
print(flat) 