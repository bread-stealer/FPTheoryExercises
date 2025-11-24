#1st Exercise: Create a dictionary with lambdas which calculates the final damage, depending on the type of attack.
#Variable - base_damage = 40
#All weapons have a multiplier:Espada (1.2), Arco (1.1), Magia (1.5)

base_damage = 40

weapons = {
    "sword": lambda dmg: dmg * 1.2,
    "bow ": lambda dmg: dmg * 1.1,
    "magic": lambda dmg: dmg * 1.5
}

print("\n")
print("Calculating final damage for different weapons:")
for weapon, calc_damage in weapons.items():
    final_damage = calc_damage(base_damage)
    print(f"{weapon.capitalize()}","|", "final damage: {final_damage}")
print("\n")