"""
RPG Character Class Exercise
============================

Your task: Implement the Character class below according to the specifications.

REQUIREMENTS:
1. The __init__ method should accept name, character_class, and starting_level (default 1)
2. Set initial stats based on character class:
   - "warrior": health=120, attack=15, defense=10
   - "mage": health=80, attack=25, defense=5
   - "rogue": health=100, attack=20, defense=8
3. Implement take_damage(amount) - reduces health by (amount - defense), minimum 1 damage
4. Implement attack_enemy(enemy) - deals attack damage to another character
5. Implement is_alive() - returns True if health > 0
6. Implement level_up() - increases level by 1 and boosts stats by 10%
7. Implement __str__() - returns a formatted string with character info

BONUS CHALLENGES:
- Add a heal(amount) method
- Prevent health from going below 0 or above a maximum
- Add a special_ability() method unique to each class
"""

class Character:
    def __init__(self, name, character_class, starting_level=1):
        # TODO: Implement initialization
        self.name = name
        self.character_class = character_class
        self.level = starting_level

        if character_class == "warrior":
            self.health = 120
            self.attack = 15
            self.defense = 10
        
        elif character_class == "mage":
            self.health = 80
            self.attack = 25
            self.defense = 5

        elif character_class == "rogue":
            self.health = 100
            self.attack = 20
            self.defense = 8
    
    def take_damage(self, amount):
        # TODO: Implement damage calculation
        self.health -= max(1, amount - self.defense)
        if self.health < 0:
            self.health = 0
    
    def attack_enemy(self, enemy):
        # TODO: Implement attack
        enemy.take_damage (self.attack)

    def is_alive(self):
        # TODO: Check if character is alive
        if self.health > 0:
            return True
        else:
            return False
    
    def level_up(self):
        # TODO: Increase level and stats
        self.level += 1
        self.health = int(self.health * 1.1)
        self.attack = int(self.attack * 1.1)
        self.defense = int(self.defense * 1.1)
    
    def __str__(self):
        # TODO: Return character info string
        return(f"Name: {self.name}, Class:{self.character_class},"
            f"Level:{self.level}, Health:{self.health},"
            f"Attack:{self.attack}, Defense:{self.defense}")


if __name__ == "__main__":
    # Create characters
    hero = Character("Aria", "warrior", 1)
    enemy = Character("Goblin", "rogue", 1)
    
    print(hero)
    print(enemy)
    print()
    
    # Battle simulation
    print("=== BATTLE START ===")
    round_num = 1
    while hero.is_alive() and enemy.is_alive():
        print(f"\nRound {round_num}")
        hero.attack_enemy(enemy)
        print(f"Hero attacks! Enemy health: {enemy.health}")
        
        if enemy.is_alive():
            enemy.attack_enemy(hero)
            print(f"Enemy attacks! Hero health: {hero.health}")
        
        round_num += 1
    
    print("\n=== BATTLE END ===")
    if hero.is_alive():
        print("Hero wins!")
        hero.level_up()
        print(f"Hero leveled up to level {hero.level}!")
    else:
        print("Hero defeated!")
