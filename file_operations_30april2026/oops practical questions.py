# ### 1. Student Class

# Create a class named Student.

# Add a class attribute school_name = "ABC School"
# Create two objects.
# Display the school name using both objects.


class Student:
    school_name="ABC School"

shab=Student()
mish=Student()
print(shab.school_name)
print(mish.school_name)

# ##2.Mobile Class

# Create a class named Mobile.

# Add class attributes:
# brand = "Samsung"
# country = "Korea"
# Create an object and print both attributes.


class Mobile:
    brand="Samsung"
    country="korea"
mobiles=Mobile()
print(mobiles.brand)

print(mobiles.country)

# ### 3. Employee Class

# Create a class named Employee.

# Add a method show_company() that prints:
# "Company Name: TechSoft"
# Create an object and call the method.


class Employee:
    def show_company(self):
        print("Company Name: TechSoft")
    
hi=Employee()
hi.show_company()

# ###4. Car Class

# Create a class named Car.

# Add class attribute wheels = 4
# Create two objects.
#Print the number of wheels using both objects.


class Car:
    wheels=4

sha=Car()
bin=Car()
print(sha.wheels)
print(bin.wheels)





