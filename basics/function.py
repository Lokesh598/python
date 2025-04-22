# def function_name(parameter: data_type) -> return_type:
#     """Docstring"""
#     # body of the function
#     return expression

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

# Assign funtion to a variable 

def a() -> int:
    return 5

b = a

b()