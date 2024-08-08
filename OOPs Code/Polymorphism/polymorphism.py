# Method Overriding
# Function call will follow Child Class

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a Phone")
        
class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone")

s = SmartPhone(20000,"OnePlus",64)

s.buy()

# We dont invoke parent constructor So,the self._num does not return

# Example 3

class Parent:
    
    def __init__(self,num):
        self.__num = num
        
    def get_num(self):
        return self.__num
    
class Child(Parent):
    
    def __init__(self,val,num):
        self.__val = va;
        
    def get_val(self):
        return self.__val
    
son = Child(100,10)
print("Parent: Num", son.get_num())

# Method Overloading
class Geometry:
    
    def area(self,a,b=None):
        if b==None:
            print("Circle",3.14*a*a)
        else:
            print("Rect",a*b)
    
obj = Geometry()
obj.area(4)
obj.area(4,5)
