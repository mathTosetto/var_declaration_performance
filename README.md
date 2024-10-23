# Variable Declaration Performance Test

This project contains a Python script that measures the time it takes to declare variables for different data types using their respective constructors and literal syntax.

## Data Types Measured

1. **List**
    - `list()`
    - `[]`
    
2. **Dictionary**
    - `dict()`
    - `{}`
    
3. **Tuple**
    - `tuple()`
    - `()`
    
4. **String**
    - `str()`
    - `''`
    
5. **Integer**
    - `int()`
    - `0`

## How the Script Works

The script uses Python's `timeit` module to run each variable declaration **1 million times**. It then compares the performance between the function constructor (e.g., `list()`, `dict()`, `tuple()`, `str()`, `int()`) and the literal syntax (e.g., `[]`, `{}`, `()`, `''`, `0`).

### How to Run

1. Clone the repository or download the `time_var_declaration.py` script.
2. Make sure Python is installed on your machine (version 3.x or higher).
3. Open your terminal and navigate to the script's directory.
4. Run the following command:

    ```bash
    python time_var_declaration.py
    ```

### Example Output


How to Run the Script:
Clone or download the Python script.
Ensure you have Python 3.x installed.
Run the script using:
bash
Copia codice
python time_var_declaration.py
Expected Output:
The output will show the time it takes to declare each data type using both literals and constructors, and then compare which method is faster. Typically, the literal syntax will be faster due to the overhead of function calls in the constructors.