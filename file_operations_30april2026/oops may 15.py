## code using constructor method

# class Student:
#     school_name="Qis"
#     course="python full stack"

#     def __init__(self):
#         print("constructor method created")

# shabin=Student()
# shahal=Student()


# class Student:
#     school_name="Qis"
#     course="python full stack"

#     def __init__(self,name,age,email,s_id):     ## if we are mentioning parameters other than self we should update it to object , if we didnt mention parameters to object it will show error
#         print("constructor method created")

# shabin=Student()
# shahal=Student()



class Student:
    school_name="Qis"
    course="python full stack"

    def __init__(self,s_id,name,age,email):
        print("constructor method created")

shabin=Student(12,"shabin",20,"shabin@gmail.com")
# shahal=Student()


##instance attribute

class Student:
    school_name="Qis"
    course="python full stack"

    def __init__(self,name,age,s_id):
        self.name=name
        self.s_age=age
        self.id=s_id

    def get_details(self):
        print(f"Student id: {self.id}\nStudent name: {self.name}")
        print(f"Age: {self.s_age}")

    

shabin=Student("shabin",21,15)
shabin.get_details()



class Employee:
    company_name="Quest"
    branch_name="calicut"

    def __init__(self,emp_id,name,salary,email):
        self.emp=emp_id
        self.name=name
        self.salary=salary
        self.email=email

    def get_details(self):
        print(f"Employee_id: {self.emp}\n Employee name: {self.name}")
        print(f"Employee Salary: {self.salary}\n Employee email: {self.email}")
    
    def update_salary(self):
        if self.salary>100000:
            increment=self.salary*0.15
            self.salary+=increment
            print(f"Updated Salary: {self.salary}")
    
    def update_company(self):
        self.company_name="Qis"
        print(f"Updated Company: {self.company_name}")

    

        
    



       
mishal=Employee(12,"misha",200000,"mishal@gmail.com")
mishal.get_details()

shab=Employee(13,"shab",300000,"shab@gmail.com")
shab.update_salary()

























