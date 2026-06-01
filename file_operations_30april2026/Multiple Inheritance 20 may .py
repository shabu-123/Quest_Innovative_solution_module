class Father:
    def drive(self):
        print("Father can drive manual")

class Mother:
    def drive(self):
        print("Mother can drive automatic")

class Son(Father,Mother):           ### MRO = Method Resolution Order   in this father will be the first priority whichever we are taking first we will select that.
    def study(self):
        print("Son can study")

Rahul = Son()
Rahul.drive()
Rahul.study()
Son.mro()       ## child class.mro()


## Hierarchical Inheritance

class Shape:
    def color(self):
        print("all shapes have colors")
    
class Rectangle(Shape):
    def area(self,l,b):
        print("area of rectange:",l*b)
    
class Circle(Shape):
    def area(self,r):
        print("area of circle: ", 3.14*r**2)

c2=Circle()
c2.area(3)

r2=Rectangle()
r2.area(3,5)

## hybrid inheritance 

class Vehicle:
    def fuel_type(self):
        print("Vehicles use some fuel type.")

# Level 1
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Motorcycle(Vehicle):
    def wheels(self):
        print("Motorcycle has 2 wheels")

# Level 2 (Hybrid)

class ElectricCar(Car):
    def battery(self):
        print("Electric Car uses lithium battery.")

class ElectricMotorcycle(Motorcycle):
    def battery(self):
        print("Electric Motorcycle uses lithium battery")


ac=ElectricCar()
ec=ElectricMotorcycle()
ac.battery()
ac.wheels()
ac.fuel_type()

ec.battery()
ec.wheels()
ec.fuel_type()



### build a food delivery app using multiple inheritance

# User
# deliverypartner
# shop
# swiggy child class

class User:
    user_name="shabin"
    def cash(self):
        print("User paid cash")
    def order(self):
        print("user ordered food")

class Deliverypartner:
    delivery_partner_name="Rahul"
    def location(self):
        print("Delivery partner has reached location")

class Shop:
    shop_name="Traders"
    def orderpacked(self):
        print("workers have packed items")

class Swiggy(User,Deliverypartner,Shop):
    swiggy_name="swiggy"
    def packeditems(self):
        print("Swiggy has packed items")

food_delivery_app=Swiggy()
food_delivery_app.cash()
food_delivery_app.order()
food_delivery_app.location()
food_delivery_app.orderpacked()
food_delivery_app.packeditems()
food_delivery_app.swiggy_name









