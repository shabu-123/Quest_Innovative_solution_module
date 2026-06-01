## single inheritance

class Animal:

    def eat(self):
        print("Animal eats food")
    
    def sleep(self):
        print("Animal sleep")

class Dog(Animal):
    pass

arjun=Dog()
arjun.eat()
arjun.sleep()




class Animal:

    def eat(self):
        print("Animal eats food")
    
    def sleep(self):
        print("Animal sleep")

class Dog(Animal):
    
    def run(self):
        print("animal runs....")

arjun=Dog()
arjun.eat()
arjun.sleep()
arjun.run()


# dog=Animal()
# dog.run()

class Person:
    def __init__(self,name,age):
        print("Calling Parent Constructor......")
        self.name=name
        self.age=age

    def get_details(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Student(Person):
    pass

richu=Student("shabin",22)



class Person:
    def __init__(self,name,age):
        print("Calling Parent Constructor......")
        self.name=name
        self.age=age

    def get_details(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Student(Person):
    def __init__(self,student_id,course):
        print("Calling child constructor.....")
        

richu=Student("shabin",22)


class Person:
    def __init__(self,name,age):
        print("Calling Parent Constructor......")
        self.name=name
        self.age=age

    def get_details(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    
    def test(self):
        print("Testing parent class")

class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course
        print("Calling child constructor.....")
        
    def test(self):
        print("Testing child class")

richu=Student("shabin",23,"python")



## multilevel inheritance

# class Vehicle:
#     def start(self):
#         print("Vehicle can start")

# class Car(Vehicle):
#     def horn(self):
#         print("vehicle can horn")

# class Ev(Car):
#     pass

# nexa=Ev()
# nexa.horn()
# nexa.start()



class Vehicle:
    def start(self):
        print("Vehicle can start")

    def headlight(self):
        print("Vehicle can make light")

class Car(Vehicle):
    def horn(self):
        print("vehicle can horn")
    
    def headlight(self):
        super().headlight()
        print("Vehicle can fog")

class Ev(Car):
    def headlight(self):
        super().headlight()
        print("Vehicle can make bright and dim light")

nexa=Ev()
nexa.headlight()
# nexa.horn()
# nexa.start()









