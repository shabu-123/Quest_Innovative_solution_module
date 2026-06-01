### class

class Students:
    pass

richu= Students()
print(id(richu))

yaseen = Students()
print(id(yaseen))



## class using methods
class Student:
    """method"""
    def exam(self):
        print("Exam conducted on 08/05/2026")

yaseen=Student()
richu=Student()

yaseen.exam()
richu.exam()

## or

class Student:
    """method"""
    def exam(self):
        print("Exam conducted on 08/05/2026")
    
    def study(self):
        pass

yaseen=Student()
richu=Student()

yaseen.exam()
richu.exam()
