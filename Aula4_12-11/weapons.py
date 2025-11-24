#1st Dictionary
weapons = {
"Name" : "Longsword",
"Damage" : 25, 
"Weight": 8.5
}

print("\n", "Name:", weapons["Name"],"\n", "Damage:", weapons["Damage"],"\n","Weight:", weapons["Weight"])
weapons["Durability"] = 100

print(weapons,"\n")

# 2nd Dictionary
droids = {
"Name" : "K-250",
"Type" : "KX",
"Stats" : {"HP" : 200, "Strength" : 300, "Mobility" : 50}
}

print("\n", "Name:", droids["Name"],"\n", "Mobility:", droids["Stats"]["Mobility"])
droids["Stats"]["HP"] = 250
print("HP Updated:", droids["Stats"]["HP"], "\n")

#3st Dictionary
shop = {
    "Potion": {"Price" : 10, "Stock" : 5},
    "Elixir": {"Price" : 25, "Stock" : 2},
    "Antidote": {"Price" : 5, "Stock" : 10},
}

for item, details in shop.items():
    print(item, "Price:", details["Price"], "Stock:", details["Stock"])

item_name = input("Item? ").strip().lower()

if item_name in shop:
    print("Price:", shop[item_name]["Price"])

    if shop[item_name]["Stock"] > 0:
        buy = input("Buy? (yes/no) ").strip().lower()
        if buy == "yes":
            shop[item_name]["Stock"] -= 1
            print("Purchased", item_name + ". Remaining stock:", shop[item_name]["Stock"])
        else:
            print("Purchase cancelled.")
else:
    print("Item not found in shop.")