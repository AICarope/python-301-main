# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...


# Importing the math module for mathematical operations
import math

# Class created for an iphone
class Smartphone:
    def __init__(self, brand, storage, battery_life):
        self.brand = brand
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
    
    def __str__(self):
        return (f"Smartphone: Brand={self.brand}, Storage={self.storage}GB, Battery Life={self.battery_life} hours")

# Class for a book
class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count
    
    def __str__(self):
        return (f"Book: Title= {self.title}, Author= {self.author}, Page Count= {self.page_count}")

# Class for modeling a computer with the `__add__()` method to add memory
class Computer:
    def __init__(self, brand, year, memory):
        self.brand = brand
        self.year = year
        self.memory = memory

    def __str__(self):
        return (f"Computer: Brand={self.brand}, Year={self.year}, Memory= {self.memory}")

    # Overload the + operator to add memory two computers
    def __add__(self, other):
        if isinstance(other, Computer):
            return self.memory + other.memory
        return NotImplemented

# Creating two instances of each class
smartphone1 = Smartphone("samsum", 128, 24)
smartphone2 = Smartphone("apple", 256, 36)

book1 = Book("AI superpowers", "AuthorKAI", 500)
book2 = Book("Anna K", "Leo Tolstoy", 800)

computer = Computer("ThinkPad", 350, "A+")
computer2 = Computer("Toshiba", 500, "A++")

# Changing some attributes
smartphone1.storage = 64
book1.page_count = 320
computer.memory = "B"

# Printing out the attributes using the __str__ method
print(smartphone1)
print(smartphone2)
print(book1)
print(book2)
print(computer)
print(computer2)

# Demonstrating the __add__ method with Computer instances
memory_total = computer + computer
print(f"The total memory of both computers is: {memory_total}")