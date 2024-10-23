# Variable Declaration Performance Test

This project contains a Python script that measures the time it takes to declare variables for different data types using their respective constructors and literal syntax.

---

## Data Types Measured

1. **List**
    - Function: `list()`
    - Literal: `[]`
    
2. **Dictionary**
    - Function: `dict()`
    - Literal: `{}`
    
3. **Tuple**
    - Function: `tuple()`
    - Literal: `()`
    
4. **String**
    - Function: `str()`
    - Literal: `''`
    
5. **Integer**
    - Function: `int()`
    - Literal: `0`

---

## How the Script Works

The script uses Python's `timeit` module to run each variable declaration `1,000,000` times. It then compares the performance between the function constructor and the literal syntax.

---

### How to Run

1. Clone the repository or download the `time_var_declaration.py` script.
2. Make sure Python is installed on your machine (version 3.x or higher).
3. Open your terminal and navigate to the script's directory.
4. Run the following command:
    ```bash
    python time_var_declaration.py
    ```

---

### Example Output
```python
Int results:
Function declaration: 0.01401954 seconds.
Literal declaration: 0.00408096 seconds.
Declaring Int using literals is faster by 70.89%.
