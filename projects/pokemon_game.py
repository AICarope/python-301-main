# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


class Pokemon:
    def __init__(self, name, p_type, level):
        self.name = name
        self.type = p_type
        self.level = level
        self.max_health = level * 5
        self.current_health = self.max_health
        self.is_knocked_out = False

    def __repr__(self):
        return f"{self.name} - Level {self.level} - Type: {self.type} - Health: {self.current_health}/{self.max_health}"

    def lose_health(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            self.is_knocked_out = True
            print(f"{self.name} has been knocked out!")

    def regain_health(self, heal):
        if self.is_knocked_out:
            print(f"{self.name} is knocked out and cannot regain health.")
        else:
            self.current_health += heal
            if self.current_health > self.max_health:
                self.current_health = self.max_health

    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print(f"{self.name} is knocked out and cannot attack.")
        else:
            effectiveness = 1
            if self.type == "Fire" and other_pokemon.type == "Grass":
                effectiveness = 2
            elif self.type == "Grass" and other_pokemon.type == "Water":
                effectiveness = 2
            elif self.type == "Water" and other_pokemon.type == "Fire":
                effectiveness = 2

            damage = self.level * effectiveness
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            other_pokemon.lose_health(damage)

# Creating two Pokemon objects
charmander = Pokemon("Charmander", "Fire", 5)
bulbasaur = Pokemon("Bulbasaur", "Grass", 5)

# Simulating a battle
charmander.attack(bulbasaur)
bulbasaur.attack(charmander)
bulbasaur.regain_health(10)
print(charmander)
print(bulbasaur)