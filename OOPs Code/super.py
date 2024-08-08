# Super keyword 
# Example 4

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
        super().buy()

s = SmartPhone(20000,"OnePlus",64)

s.buy()


# Example 5

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

        
class SmartPhone(Phone):
    
    def __init__(self,price,brand,camera,os,ram):
        print("Pehle yahan")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")

s = SmartPhone(20000,"OnePlus",64,"Android",8)

print(s.os)
print(s.ram)
