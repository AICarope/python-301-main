# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

#1
class Movie:
#2
    def __init__(self, year, title):
        self.year = year
        self.title = title
#3
class RomCom(Movie):
    pass

#4
class ActionMovie(Movie):
    def __init__(self, year, title, pg=13):
        super().__init__(year, title)  # Call the superclass's __init__ method
        self.pg = pg
