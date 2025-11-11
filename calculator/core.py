# calculator/core.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def sub(a, b):
    """Return the difference of two numbers."""
    return a - b


def mul(a, b):
    """Return the product of two numbers."""
    return a * b


def div(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b
