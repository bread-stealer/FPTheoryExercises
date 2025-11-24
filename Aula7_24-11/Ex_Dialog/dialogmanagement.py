# 1ST EXERCISE
# Dialog management
# 1- Use the dialogos.txt file in Moodle and print all lines in the file.
# 2 - Separate each line in the file by name and speech.
# 3 - Build a dictionary in which the names are the keys and the speeches are the values.
# 4 - Serialize the dictionary into a JSON file – dialogos.json
# 5 - Create an executable program that reads any dialogos.txt file and transforms it into a dialogos.json file.
# 6 - This executable should ask the user for the ID of an existing NPC and print only the speeches of that NPC.

import json

# 1ST STEP
# Read and print all lines in the dialogos.txt file
file = open("dialogos.txt", "rt")
all_files = file.readlines()

print("All Lines in File")
for line in all_files:
    print(line.strip())
print()

# 2ND STEP & 3RD STEP
# Separate each line by name and speech, and build a dictionary
dialog_dict = {}

for line in all_files:

    if ":" in line and line.strip() != "":
        parts = line.split(":", 1)
        name = parts[0].strip()
        speech = parts[1].strip()

        if name in dialog_dict:
            dialog_dict[name].append(speech)
        
        else:
            dialog_dict[name] = [speech]

file.close()
print("Dialog Dictionary")
print(dialog_dict)
print()

# 4TH STEP
# Serialize the dictionary into a JSON file – dialogos.json
open_file = open("dialogos.json", "wt")
json.dump(dialog_dict, open_file)
open_file.close()

print("Json File Created")
print()

# 5TH STEP & 6TH STEP
# Ask user for NPC ID and print only that NPC's speeches
print("NPC Search - Available NPCs:")

for npc_name in dialog_dict:
    print(npc_name)
print()

npc_id = input("Enter the ID (name) of an existing NPC: ").strip()

if npc_id in dialog_dict:
    print ("Speeches of", npc_id)
    print()
    for speech in dialog_dict[npc_id]:
        print(speech.strip())
        print()

else:
    print("NPC not found in the dialog file.")