def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b

def calculate_result(a, b, c):
    """
    Integration function:
    1. Add a and b.
    2. Multiply the sum by c.
    3. Subtract b.
    4. Divide the result by c.
    """
    sum_result = add(a, b)
    multiplication_result = multiply(sum_result, c)
    subtraction_result = subtract(multiplication_result, b)
    final_result = divide(subtraction_result, c)

    return final_result