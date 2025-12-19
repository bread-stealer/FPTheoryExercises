"""
Exercise: Make the List Sum to Zero

You have a list of numbers. Your task is to modify the list so that 
when you sum all its elements, the result is exactly 0.

Rules:
- You can add numbers to the list
- You can remove numbers from the list
- You can change existing numbers
- The final list must sum to exactly 0

Try different approaches!
"""

# Starting list
numbers = [5, 10, -3, 7, 2]

# TODO: Modify the 'numbers' list here to make it sum to 0
# Your code here:
sum_num = (sum(numbers) * 0)
print(f"List Multiplying for Zero: {sum_num}") # Multiply the sum by 0

numbers.append(-sum(numbers)) # Adding -21 to the List, [5, 10, -3, 7, 2, -21]
print(f"List Sum to Zero: {sum(numbers)}") # Sums all values: 5+10+(-3)+7+2+(-21) = 0




