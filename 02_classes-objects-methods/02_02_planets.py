# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet:
    def __init__(self, name, radius, mass, orbital_period, distance_from_sun):
        self.name = name
        self.radius = radius #kilometers km
        self.mass = mass #in km
        self.orbital_period = orbital_period # in earth days
        self.distance_from_sun = distance_from_sun #in km 
    def __str__(self):
        return (f"planet name:{self.name}")
        return (f"radius:{self.radius}")
        return(f"mass: {self.mass}")
        return(f"orbital_period: {self.orbital_period}")
        return(f"distance_from_sun{self.distance_from_sun}")
     
#instantiate: activate the class, to create Planet
earth = Planet(name="Earth", radius=6371, mass=5.972e24, orbital_period=365.25, distance_from_sun=1.496e8)
# Print the planet's information
print(earth)
print(earth.distance_from_sun)