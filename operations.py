def addition(a,b):
    result = a + b
    return result
def subtraction(a,b):
    result = a - b
    return result
def multiplication(a,b):
    result = a * b
    return result
def division(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divine by zero")
    result = a / b
    return result

