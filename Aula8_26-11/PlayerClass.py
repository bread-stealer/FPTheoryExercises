# Player with position and stamina - Create a Player class with:
#   attributes: name, x, y, stamina
#   constructor that receives name, x, y, and stamina
#   methods: 
#   log() → prints position and stamina
#   move(dx, dy) → changes x and y and reduces stamina by 1 for each movement (even if diagonal)
#   is_exhausted() → returns True if stamina <= 0, otherwise False

class Player:
    def __init__(self, name, x, y, stamina):
        self.name = name
        self.x = x
        self.y = y
        self.stamina = stamina
    
    def log(self):
        print(f"Player: {self.name}")
        print(f"Position: ( {self.x} , {self.y} )")
        print(f"Stamina: {self.stamina}")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.stamina -= 1
    
    def is_exhausted(self):
        return self.stamina <= 0
