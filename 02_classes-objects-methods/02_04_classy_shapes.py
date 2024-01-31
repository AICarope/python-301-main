# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle:
    def__init__(self, radius):
    self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

#instantiate: activate the class, to create rectangle object
rectangle = Rectangle (length= 10, width = 3)
print (f"the area of the rectangle is: {rectangle.area()}")
print (f"the perimeter of the rectangle is: {rectangle.perimeter()}")

#instantiate: activate the class, to create circle object
circle = Circle (radius= 60)
print(f"the area of the circle is: {circle.area()}")
print(f"the perimeter of the circle is: {circle.perimeter()}")
         