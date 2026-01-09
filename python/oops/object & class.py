#creating class
class Dog:
    pass

#/////////////////////////////////////////////////
class Car:
    def printCar(self):
        print("ferrari")

#creating object
ob = Car()
ob.printCar()

# ////////////////////////////////////////////////
class Number:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number
    

ob = Number(7)

print(ob.returnNumber())

#//////////////////////////////////////////////////
class Vehicle:
    # __init__ used to initate class means its like constructor
    
    def __init__(self, name, brand, price, color):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

    def printCarDescription(self):
        
        return "%s is a %s %s worth $%.2f." %(self.name, self.brand, self.color, self.price)


car = Vehicle("Supra", "Toyota", 400000.00, "yellow")
print(car.printCarDescription())

#///////////////////////////////////////////////////
class Vehicle:
    #...data members
    name = "Supra"
    brand = "Toyota"
    color = "yello"
    price = 400000

    def printCarDescription(self):
        
        return "%s is a %s %s worth $%.2f." %(self.name, self.brand, self.color, self.price)


car = Vehicle()
print(car.printCarDescription())

#///////////////////////////////////////////////////






