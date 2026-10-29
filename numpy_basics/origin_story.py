"""
=============================================================================
MODULE: NumPy Fundamentals - Origin, Purpose, and Impact
=============================================================================
This script explains who created NumPy, why it was built, and how it 
revolutionized numerical computing in Python.
=============================================================================
"""

import numpy as np

# =============================================================================
# 1. WHO CREATED NUMPY AND WHY?
# =============================================================================
"""
- Creator: Travis Oliphant
- Year: 2005
- Why was it built?: 
  In the early days of Python, doing heavy math or working with large grids of 
  numbers was extremely painful and slow. Different developer groups built 
  separate, competing libraries ('Numeric' and 'Numarray'). This created confusion 
  and fragmentation.
  
  In 2005, Travis Oliphant decided to fix this mess. He took the best parts of 
  both libraries and merged them into a single, unified standard library: 
  NumPy (Numerical Python).
"""


# =============================================================================
# 2. HOW THINGS CHANGED AFTER NUMPY ARRIVED
# =============================================================================
"""
Before NumPy:
- Python was treated mostly as a scripting language. Heavy numerical calculations 
  were done in C or Fortran because standard Python lists were too slow and 
  inefficient for memory.
- Doing math on lists required writing slow 'for' loops, because Python had to 
  dynamically check the data type of every single item.

After NumPy:
- Contiguous Memory: NumPy introduced arrays where data is stored in a single, 
  unbroken block in RAM, letting the CPU load and process data instantly.
- Vectorization: Developers could suddenly perform math on entire arrays of data 
  at once without writing loops.
- The Birth of Modern AI & Data Science: NumPy became the foundational bedrock. 
  Libraries like Pandas, SciPy, Scikit-Learn, PyTorch, and TensorFlow were built 
  directly on top of NumPy's array architecture. 
  
In short, NumPy turned Python from a simple scripting language into a powerhouse 
for Artificial Intelligence, Data Science, and Scientific Computing.
"""


# =============================================================================
# 3. PRACTICAL CODE EXAMPLE: BEFORE VS AFTER
# =============================================================================

# Scenario: Multiplying every element in a dataset by 2.

# --- THE OLD WAY (Normal Python List) ---
# Requires a slow loop because Python cannot perform direct vector math on lists.
python_list = [10, 20, 30, 40, 50]
list_result = [x * 2 for x in python_list]

# --- THE NEW WAY (NumPy Array) ---
# Direct vectorization: Executes instantly under the hood using C-level optimization.
numpy_array = np.array([10, 20, 30, 40, 50])
numpy_result = numpy_array * 2

print("Python List Result :", list_result)
print("NumPy Array Result :", numpy_result)