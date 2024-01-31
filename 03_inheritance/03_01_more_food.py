# 1 Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# 2 Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.



class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")
#1
class Meats(Ingredient):
        """Models a meat type."""

    def expire(self):
        """Overrides the expire method to include expiration date."""
        print(f"Oh no! The {self.name} are very old do not eat these on {self.expiration_date}")
        self.name = "expired " + self.name

    def super_expired(self, current_date):
        """Checks if the product has expired."""
        if current_date > self.expiration_date:
            print(f"The {self.name} has already expired.")
            return True
        else:
            print(f"The {self.name} is still good, so you can consume it.")
            return False

    def freshness(self):
        print(f"You have now {self.freshness} of meat type {self.name}.")

    
chicken = Meats ('checken' , '1 leg', '2024-01-10')
print(chicken)

#HELP: with the overriding 