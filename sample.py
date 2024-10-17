# example.py

def add_numbers(a, b):
    """
    This function adds two numbers.
    """
    return a + b

def unused_function():
    """
    This function is never called and serves as an example of an unused function.
    """
    result = 10 + 5  # This variable is unused
    return result

def divide_numbers(a, b):
    """
    This function divides two numbers and handles division by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def insecure_code():
    """
    This function demonstrates a potential security vulnerability by using eval().
    """
    user_input = "2 + 2"
    result = eval(user_input)  # Warning: This can execute arbitrary code!
    return result

if __name__ == "__main__":
    print("Add 2 and 3:", add_numbers(2, 3))
    print("Divide 10 by 2:", divide_numbers(10, 2))
    # Call the unused function to see it won't be detected in CodeQL
    unused_function()

