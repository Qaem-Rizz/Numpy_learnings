# ==============================================================================
# PYTHON ARRAYS TUTORIAL! 🚀
# Think of this file as a complete, friendly guide to understanding 
# arrays in Python. You can run this entire script directly using Python!
# ==============================================================================

"""
--------------------------------------------------------------------------------
1. WHAT IS AN ARRAY? (The Core Idea)
--------------------------------------------------------------------------------
Imagine you have 5 different balls. Instead of putting each ball in a separate 
box (creating 5 different variables), you put all 5 balls inside ONE long 
organizer box. 

That organizer box is an ARRAY!

In Python, the most common and easiest way to make an array is by using a LIST.
Lists store multiple items inside square brackets: [...]
"""

# ==============================================================================
# 2. 1D ARRAY (ONE-DIMENSIONAL ARRAY)
# ==============================================================================
# REAL-LIFE ANALOGY: A single line of students or a daily shopping list.

# --- Syntax ---
# array_name = [item1, item2, item3, ...]

# --- Example ---
fruits = ["Apple", "Banana", "Cherry", "Mango"]

print("--- 1D Array Basics ---")
print("Complete List of Fruits:", fruits)

# --- How to Access Items (Indexing) ---
# In Python, counting starts at 0!
# Index 0 -> 1st item
# Index 1 -> 2nd item
print("First fruit (Index 0):", fruits[0])   # Output: Apple
print("Second fruit (Index 1):", fruits[1])  # Output: Banana

# --- Adding and Removing Items ---
fruits.append("Orange")  # Adds "Orange" to the end
print("After adding Orange:", fruits)

fruits.remove("Banana")  # Removes "Banana"
print("After removing Banana:", fruits)

# --- Finding Length ---
print("Total number of fruits:", len(fruits))


print("\n" + "="*50 + "\n")


# ==============================================================================
# 3. 2D ARRAY (TWO-DIMENSIONAL ARRAY)
# ==============================================================================
# REAL-LIFE ANALOGY: A chessboard, a movie theater seating plan, or an Excel sheet.
# A 2D array is simply a list of lists! It has ROWS and COLUMNS.

# --- Syntax ---
# array_2d = [
#     [row0_col0, row0_col1],
#     [row1_col0, row1_col1]
# ]

# --- Example: Classroom Seating Chart ---
# 3 Rows of students, 3 Seats in each row
classroom = [
    ["Alice", "Bob", "Charlie"],     # Row 0
    ["David", "Emma", "Frank"],      # Row 1
    ["Grace", "Henry", "Isabella"]   # Row 2
]

print("--- 2D Array Basics ---")
print("Full Classroom Seating Layout:")
for row in classroom:
    print(row)

# --- How to Access Specific Items ---
# Syntax: array_name[row_index][column_index]

# Goal: Find the student in Row 1, Column 2 (0-indexed -> 2nd row, 3rd seat)
student = classroom[1][2]
print("\nStudent at Row 1, Column 2:", student)  # Output: Frank

# --- Changing a Value ---
# Suppose Alice (Row 0, Column 0) transfers out, and "John" takes her seat:
classroom[0][0] = "John"

print("\nUpdated Classroom Layout (Alice replaced by John):")
for row in classroom:
    print(row)


print("\n" + "="*50 + "\n")


# ==============================================================================
# 4. QUICK SUMMARY & BEST PRACTICES
# ==============================================================================
"""
KEY TAKEAWAYS:
1. 1D Array = Single line of items -> list[index]
2. 2D Array = Grid with Rows & Columns -> list[row_index][column_index]
3. Python arrays (lists) start counting position numbers from ZERO (0).
4. Use .append() to add items and .remove() to delete items.
"""

print("Tutorial Complete! Happy Coding ")