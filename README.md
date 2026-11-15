# NumPy Learnings
 
My personal notes and practice scripts from learning NumPy. Each concept has its own small, runnable `.py` file with comments explaining what it does and why it matters.
 
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
 
---
 
## What's inside
 
| Folder | What I practiced |
|---|---|
| `numpy_basics/` | Where NumPy came from, creating arrays, `np.arange()`, `np.eye()` |
| `Numpy_arrays/` | `.shape`, `.size`, `.ndim`, `.dtype`, `.astype()` |
| `operations/` | Element-wise arithmetic without loops |
| `Aggregation/` | `sum`, `mean`, `std`, `var`, `min`, `max`, `prod`, `cumsum`, `cumprod` |
| `indexing_slicing/` | Indexing, slicing, fancy indexing, boolean masking |
| `Reshaping and Manipulating/` | `reshape()`, `flatten()` vs `ravel()` |
| `Advance_Numpy/` | `append`, `insert`, `delete`, `concatenate`, `vstack`/`hstack`, splitting |
| `Broadcasting/` | Broadcasting rules, 1D to 2D, what breaks when shapes don't match |
| `vectorisation/` | Loop-based vs vectorized code |
| `Handling_missing_values/` | `isnan`, `isinf`, `nan_to_num` |
 
---
 
## A few things I found worth noting
 
**Vectorization vs loops**
```python
# plain Python
result = [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
 
# NumPy
result = np.array([1, 2, 3]) + np.array([4, 5, 6])   # [5 7 9]
```
 
**Boolean masking**
```python
arr = np.array([10, 20, 30, 40, 50])
arr[arr > 30]    # [40 50]
```
 
**`flatten()` vs `ravel()`**: `flatten()` returns a copy, `ravel()` returns a view, so changing the ravelled array can change the original.
 
**Broadcasting**: adding a 1D array to a 2D array works row-wise when the shapes are compatible. If not, NumPy raises a `ValueError`.
 
---
 
## Running the scripts
 
```bash
git clone https://github.com/Qaem-Rizz/Numpy_learnings.git
cd Numpy_learnings
pip install numpy
python Broadcasting/broadcasting.py
```
 
Every script is standalone, so any file can be run on its own.
 
---
 
## Why I made this
 
I wanted to move from plain Python lists to array-based computing, which is the base for data analysis and ML work. Writing a small script per concept helped me understand each one properly instead of just reading about it.
 
Still adding to it as I learn more (linear algebra, `np.random`, sorting/searching).
 
---
 
Built by **Qaem Hussain Rizvi**
 