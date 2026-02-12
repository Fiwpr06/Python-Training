# Init classes
class NPC:
    """Representing a non-player character in a game."""
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def attack(self, target):
        """Outputs an attack message and reduces the target's HP."""
        print(f"{self.name} attacks {target.name}!")
        target.hp = max(0, target.hp - 10)
        print(f"{target.name} has {target.hp} HP left.", end="\n\n")
        
class Player(NPC):
    """Subclass of NPC representing a player character in a game."""
    def __init__(self, name, hp, level):
        super().__init__(name, hp)
        self.level = level
        
    def level_up(self):
        """Increases the player's level by 1 and outputs a level-up message."""
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")
        
class Enemy(NPC):
    """Subclass of NPC representing an enemy character in a game."""
    def __init__(self, name, hp, enemy_type):
        super().__init__(name, hp)
        self.enemy_type = enemy_type
        
    def taunt(self):
        """Outputs a taunt message from the enemy."""
        print(f"\n{self.name} the {self.enemy_type} taunts you!", end="\n\n")

# Example usage
player1 = Player("Hero", 100, 1)
enemy1 = Enemy("Goblin", 20, "Warrior")
enemy1.taunt()
while(enemy1.hp > 0 and player1.hp > 0):
    player1.attack(enemy1)
    if enemy1.hp > 0:
       enemy1.attack(player1)
       
if enemy1.hp <= 0:
    print(f"{enemy1.name} has been defeated!")
    player1.level_up()
if player1.hp <= 0:
    print(f"{player1.name} has been defeated!")
