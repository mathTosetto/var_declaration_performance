import timeit


def time_declaration(code_str: str, iterations: str = 1000000) -> float:
    """
    This function times how long it takes to declare a variable using the provided code string.

    Args:
        code_str (str): The code to declare the variable, e.g., "var = list()" or "var = []"
        iterations (int): The number of times the declaration should be repeated

    Returns:
        float: The time taken to declare the variable in seconds for the given iterations
    """
    return timeit.timeit(code_str, number=iterations)


def compare_times(var_type: str, function_time: float, literal_time: float):
    """
    Compares the timing results between function constructor and literal declaration,
    and calculates the percentage difference in speed.

    Args:
        var_type (str): The type of variable being compared (e.g., "List", "Dictionary").
        function_time (float): The time taken to declare the variable using the function constructor.
        literal_time (float): The time taken to declare the variable using the literal declaration.
    """
    print(f"-" * 40)
    print(f"{var_type} results:")
    print(f"Function declaration: {function_time:.8f} seconds.")
    print(f"Literal declaration: {literal_time:.8f} seconds.")
    if function_time > literal_time:
        faster_time = literal_time
        slower_time = function_time
        method = "literals"
    else:
        faster_time = function_time
        slower_time = literal_time
        method = "function constructors"

    percentage_faster = ((slower_time - faster_time) / slower_time) * 100

    print(
        f"Declaring {var_type} using {method} is faster by {percentage_faster:.2f}%.\n"
    )


# List timing
time_list_function = time_declaration("var = list()")
time_list_literal = time_declaration("var = []")

# Dict timing
time_dict_function = time_declaration("var = dict()")
time_dict_literal = time_declaration("var = {}")

# Tuple timing
time_tuple_function = time_declaration("var = tuple()")
time_tuple_literal = time_declaration("var = ()")

# Str timing
time_str_function = time_declaration("var = str()")
time_str_literal = time_declaration("var = ''")

# Int timing
time_int_function = time_declaration("var = int()")
time_int_literal = time_declaration("var = 0")

compare_times("List", time_list_function, time_list_literal)
compare_times("Dict", time_dict_function, time_dict_literal)
compare_times("Tuple", time_tuple_function, time_tuple_literal)
compare_times("Str", time_str_function, time_str_literal)
compare_times("Int", time_int_function, time_int_literal)
