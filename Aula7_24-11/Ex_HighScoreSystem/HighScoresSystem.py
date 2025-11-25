# High scores system
# 1 - Uses Moodle's highscore.json file, creates a dictionary with the data, and prints it. Checks to confirm that the file is not empty.
# 2 - Uses the input system to ask the user for a new name and integer score. Adds this data to the high scores
# 3 - Sorts the list of high scores by descending score (without using sort() or sorted())
# 4 - Keeps only the top 3 results
# 5 - Serializes the list of scores again as new_highscores.json
# 6 - Finally, prints the new numbered ranking (1st, 2nd, and 3rd)

import json

# 1ST STEP
# Creates a dictionary with the data from highscore.json and prints it
highscores_data = {}

file = open("highscores.json", "rt")
json_data = file.read()

highscores_data = json.loads(json_data)
print ("Highscores Data: ", highscores_data)
print()

file.close()


# 2ND STEP
# Asks the user for a new name and integer score, adds this data to the high scores
new_name = input("Enter a name: ")
new_score = int(input("Enter a score (integer): "))

new_entry = {
    "name" : new_name, 
    "score" : new_score
}

highscores_data["highscores"].append(new_entry)
print ("Updated Highscores Data: ", highscores_data)
print()

file.close()

# 3RD STEP
# Sorts the list of high scores by descending score (without using sort() or sorted())
highscores_list = highscores_data["highscores"]
n = len(highscores_list)

for i in range(n):
    for j in range( n - i - 1):
        if highscores_list[j]["score"] < highscores_list[j + 1]["score"]:
            temp = highscores_list[j]
            highscores_list[j] = highscores_list[j + 1]
            highscores_list[j + 1] = temp
            
print("Sorted Highscores List: ", highscores_list)
print()

# 4TH STEP
# Keeps only the top 3 results
highscores_data["highscores"] = highscores_list[:3]
print("Top 3 Highscores: ", highscores_data)
print()

# 5TH STEP
# Serializes the list of scores again as new_highscores.json
new_file = open("new_highscores.json", "wt")
json_string = json.dumps(highscores_data, indent=4)
new_file.write(json_string)
print("New highscores saved to new json file")
print()

new_file.close()

# 6TH STEP
# Prints the new numbered ranking (1st, 2nd, and 3rd)
print("Top 3 Rankings:")

for index, entry in enumerate(highscores_data["highscores"]):
    rank = index + 1
    suffix = "th"
    if rank == 1:
        suffix = "st"

    elif rank == 2:
        suffix = "nd"
    
    elif rank == 3:
        suffix = "rd"

    print(f"{rank}{suffix}: {entry['name']} with a score of {entry['score']}")
