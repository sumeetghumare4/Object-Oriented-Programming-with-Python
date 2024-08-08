# Single level Inheritance

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a Phone")
        
    def return_phone(self):
        print("Returnrnig a phone")
        
class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()


# Mutli level Inheritance

class Product:
    def review(self):
        print("Product customer review")
        
class Phone(Product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price  = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone")
        
class SmartPhone(Phone):
    pass

s = SmartPhone(20000,"Apple",12)
p = Phone(1000,"Samsung",1)


s.buy()
s.review()
p.review()

# Hierarchical Inheritance

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price  = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone")
        
    def return_phone(self):
        print("Returning a Phone")
        
class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()

# Multiple Inheritance

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone")
        
class Product:
    def review(self):
        print("Customer review")
        
class SmartPhone(Phone,Product):
    pass

s = SmartPhone(2000,"Apple",12)

s.buy()
s.review()

# Exmaple of Multiple 
# MRO - Method resolution Order

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone")
        
class Product:
    def buy(self):
        print("Product buy method")
        
class SmartPhone(Product,Phone): #MOR
    pass

s = SmartPhone(2000,"Apple",12)

s.buy()
