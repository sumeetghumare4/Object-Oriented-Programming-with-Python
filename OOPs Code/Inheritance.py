# Basic Udemy Examples for showing that student can access user class but user can not access student class

class User:
    
    def login(self):
        print("Login")
        
    def register(self):
        print("Register")
        
class Student(User):  # Now student is subclass of student
    
    def enroll(self):
        print("Enroll")
        
    def review(self):
        print("Review")
        
        
stu1 = Student()

stu1.enroll()
stu1.login()
stu1.register()
stu1.review()

# u = User()

# u.enroll()

# Inheriting Constructor

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
        
class SmartPhone(Phone):
    pass

s = SmartPhone(20000,"OnePlus",64)
print(s.camera)

# Inheriting Private Constructor
# child class can not access parent class hidden instance

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera
        
class SmartPhone(Phone):
    pass

s = SmartPhone(20000,"OnePlus",64)
print(s.__brand)


