# 

### Abstraction

from abc import ABC, abstractmethod


class FirstGenATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass
    
    def check_balance(self):
        pass

class NewGenATM(FirstGenATM):
    def withdraw(self):
        return "can withdraw"
    
sbi=NewGenATM()






# class FirstGenATM(ABC):

#     @abstractmethod
#     def withdraw(self):
#         pass
#     @abstractmethod
#     def check_balance(self):
#         pass

# class NewGenATM(FirstGenATM):
#     def withdraw(self):
#         return "can withdraw"
    
# sbi=NewGenATM()












## duck typing

class Animal:

    def make_sound(self):
        print("animal makes sound")


class Dog:
    def make_sound(self):
        print("Bow Bow")

class Cat:
    def make_sound(self):
        print("Meow meow")


def sound(animal):
    animal.make_sound()


a=Animal()
d=Dog()
c=Cat()

sound(a)
sound(d)
sound(c)




