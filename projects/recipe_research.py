# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

class Ingredients:
    def __init__(self, *ingredients):
        self.ingredients = ingredients

    def generate_recipe_search_url(self):
        base_url = "https://www.example.com/recipes?q="
        query = '+'.join(self.ingredients)
        return base_url + query
    
    # Creating an Ingredients object
my_ingredients = Ingredients("chicken", "broccoli", "garlic", "soy sauce")

# Generating a recipe search URL
recipe_search_url = my_ingredients.generate_recipe_search_url()
print(recipe_search_url)