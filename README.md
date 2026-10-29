# NumPy Learnings 🚀

A structured collection of notes, code snippets, and practical implementations as I learn NumPy from scratch.

---

## 📌 Overview

This repository tracks my progress learning **NumPy** (Numerical Python). The primary focus is to transition from standard Python lists to fast, array-based numerical computing for data analysis, machine learning, and performance optimization.

---

## 💡 Why NumPy?

- **C-Engine Speed:** Written in C/Fortran under the hood, running much faster than standard Python loops.
- **Contiguous Memory:** Stores elements in contiguous memory blocks for fast CPU cache access.
- **Vectorization:** Operations run on entire arrays simultaneously without explicit `for` loops.

---

## 📋 Prerequisites

Before running the code in this repository, ensure you have:

- **Python 3.8+** installed on your system.
- **Git** installed for repository cloning.
- Basic familiarity with Python syntax.

---

## ⚙️ Installation & Local Setup

Follow these steps to clone the repository and run the scripts locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Qaem-Rizz/Numpy_learnings.git
cd Numpy_learnings
```

### 2. Set Up a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install NumPy
```bash
pip install numpy
```

---

## 📚 Curriculum & Topics Covered

### 1. Introduction & Array Basics
- Difference between Python Lists vs NumPy Arrays
- Creating 1D, 2D, and Multi-Dimensional Arrays
- Array generation: `np.zeros()`, `np.ones()`, `np.arange()`, `np.full()`, `np.eye()`

### 2. Array Properties & Data Types
- Checking properties: `.shape`, `.size`, `.ndim`, `.dtype`
- Type casting with `.astype()`
- Aggregation functions: `sum()`, `mean()`, `min()`, `max()`, `std()`, `var()`

### 3. Indexing, Slicing & Reshaping
- 0-based and negative indexing
- Array slicing `[start:stop:step]`
- Fancy indexing & Boolean masking (Filtering data)
- Reshaping (`.reshape()`) and Flattening (`.ravel()` vs `.flatten()`)

### 4. Array Manipulation & Joining
- Adding elements: `np.append()`, `np.insert()`
- Joining/Combining: `np.concatenate()`, `np.vstack()`, `np.hstack()`
- Splitting arrays: `np.split()`, `np.hsplit()`, `np.vsplit()`

### 5. Broadcasting & Vectorization
- Rules of Broadcasting (matching dimensions and shape expansion)
- Performance comparison: Vectorized operations vs Python loops

### 6. Data Cleaning Workflow
- Detecting missing values with `np.isnan()` and `np.isinf()`
- Replacing missing/infinite values using `np.nan_to_num()`
- Handling outliers and data filtering techniques

---

## ⚡ Quick Code Snippet

```python
import numpy as np

# Creating a 2D array
arr = np.array([[10, 20, 30], [40, 50, 60]])

# Filtering elements greater than 25 (Boolean Masking)
filtered = arr[arr > 25]

print("Filtered Values:", filtered)  # Output: [30 40 50 60]
```

---

## 📂 Project Structure

```text
.
├── 01_basics.py          # Array creation & properties
├── 02_indexing.py        # Slicing, boolean masking & reshaping
├── 03_broadcasting.py    # Vectorization & broadcasting rules
├── 04_data_cleaning.py   # Handling NaNs and outliers
├── .gitignore            # Ignores venv and cache files
└── README.md             # Documentation
```

---

## ⭐ Support

If you found this repository cool for NumPy, feel free to give it a **Star (⭐)**!