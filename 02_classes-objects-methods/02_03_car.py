# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.


class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed #in km
        
    def __str__(self):
        return(f"model: { self.model}")
        return(f"year: {self.year}")
        return(f"max_speed: {self.max_speed}")
    
    #increases the `max_speed` of the car by 5 when called   
    def __add__(self):
        self.max_speed += 5
            
    #instantiate: activate the class, to create Car

mycar = Car (model = "Sport", year = 2022, max_speed = 200)  
    
print(mycar.year)
    