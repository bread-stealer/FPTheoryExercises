
# FIRST EXERCISE 
fleet = {
    "Red Leader" : {"X-Wing", "A-Wing"},
    "Wedge Antilles" : {"X-Wing"},
    "Poe Dameron" : {"X-Wing", "T-70", "Black One"},
    "Luke Skywalker" : {"X-Wing", "Snowspeeder" },
}

#Poe Dameron's ships
print ("\nPoe Dameron's Ships:", fleet["Poe Dameron"])

#Common Ships between Luke and Wedge Antilles
common_ships = fleet["Luke Skywalker"].intersection(fleet["Wedge Antilles"])
print ("\nCommon Ships between Luke and Wedge Antilles:", common_ships)

#Ships used by Read Lead but not by Poe Dameron
red_leader_unique = fleet["Red Leader"].difference(fleet["Poe Dameron"])
print ("\nShips used by Red Leader but not by Poe Dameron:", red_leader_unique)

#all_ships set thats contains ships shared by everyone
all_ships = set.intersection(*fleet.values())
print ("\nShips shared by everyone:", all_ships)

#Completed list of all ships
all_unique_ships = set.union(*fleet.values())
print ("\nAll Ships in the Fleet:", all_unique_ships)

# SECOND EXERCISE

