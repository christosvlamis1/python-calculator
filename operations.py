def menu():
    print("CALCULATOR")
    print("Choices")
    print("Choose 1,2,3,4.... based on what mathematical operation you wish to be used")
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    users_input = int(input("\nwhat do you wish to do:"))
    return users_input
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
    result = a / b
    return result
def showresult(a):
    print("\nresult =",a,"\n")
