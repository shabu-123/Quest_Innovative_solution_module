class Student:    ### student indicates class
    school_name="Quest Innovative Solutions"    ## school_name indicates class attribute

richu=Student()
yaseen=Student()
print(Student().school_name)

richu.school_name="qis"       ## if we are using object to update it will update to that particular object
print(richu.school_name)
print(yaseen.school_name)


richu.school_name="dhdhh"
del richu.school_name
print(richu.school_name)
del Student.school_name
# print(Student().school_name)
print(Student.school_name)
print(richu.school_name)
print(yaseen.school_name)


## class attribute have single memory space







