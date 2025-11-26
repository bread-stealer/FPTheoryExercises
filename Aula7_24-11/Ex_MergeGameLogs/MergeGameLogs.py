# Merge game logs
# 1- Use the two files in Moodle – day1.log and day2.log. Open the files and read all the lines in each of them
# 2 - Create a merged log with all the lines from both logs, each line must indicate the day in the format [DAY1] or [DAY2]
# 3 - Count the total number of lines for each day using the merged log
# 4 - Create a statistical dictionary containing the number of actions for each day and the total number of actions for both days
# 5 - Serialize the merged log into a log_stats.json file

import json

# 1ST STEP
# Open the files and read all the lines in each of them
file1 = open("day1.log", "rt")
day1_lines = file1.readlines()

print(">>> All Lines in Day1 File <<<")
for line in day1_lines:
    print(line.strip())
print()

file1.close()

file2 = open("day2.log", "rt")
day2_lines = file2.readlines()

print(">>> All Lines in Day2 File <<<")
for line in day2_lines:
    print(line.strip())
print()

file2.close()

# 2ND STEP
# Create a merged log with all the lines from both logs
# Each line must indicate the day in the format [DAY1] or [DAY2]
merged_log = []

for line in day1_lines:
    merged_log.append("[DAY1]" + line.strip())

for line in day2_lines:
    merged_log.append("[DAY2]" + line.strip())

print(">>> Merged Log <<<")
for line in merged_log:
    print(line)
print()

# 3RD STEP
# Count the total number of lines for each day using the merged log
day1_count = 0
day2_count = 0

for line in merged_log:
    if line.startswith("[DAY1]"):
        day1_count += 1
    elif line.startswith("[DAY2]"):
        day2_count += 1

print(">>> Total Count Number of Lines for Each Day <<<")
print("Total of Lines in Day1: ", day1_count)
print("Total of Lines in Day2: ", day2_count)

# 