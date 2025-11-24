# In Moodle, file exerc_aula7_fp.py:
# Each block of code contains intentional errors that cause the program to crash.
# The goal is to implement proper exception handling using:
#   try / except
#   raise
#   assert
# The goal is not to correct the errors, but only to handle them so that the code remains functional
# Do not change the logic of the program. Just make it robust

#1
def calcular_dano(base_damage, crit_chance):
    
    assert 0 <= crit_chance <= 1, "Crit chance inválida"

    if base_damage < 0:
        raise ValueError("Dano base não pode ser negativo")

    from random import random

    if random() < crit_chance:
        return base_damage * 2
    return base_damage


print(calcular_dano(50, 1.5))   # rebenta aqui



#2
class InventoryFull(Exception):
    pass

inventory = ["Sword", "Shield", "Potion"]
MAX_ITEMS = 3

def add_item(item):
    if len(inventory) >= MAX_ITEMS:
        raise InventoryFull("Inventário cheio")
    inventory.append(item)


add_item("Gem") 
print(inventory)


#3
def login(username, password):
    assert username != "", "Username vazio"

    if len(password) < 4:
        raise Exception("Password demasiado curta")

    return "Login bem sucedido"


print(login("", "12"))


#4
class OutOfMap(Exception):
    pass

def move_player(x, y):
    if x < 0 or y < 0 or x > 5 or y > 5:
        raise OutOfMap("Movimento fora do mapa")

    return (x, y)


pos = (2, 2)
print(move_player(10, 1)) 
