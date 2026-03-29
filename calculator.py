import operations as op
import os

width = os.get_terminal_size().columns

options = ["1","2","3","4"]

def in_options():
    users_input = ""
    while users_input not in options: 
        users_input = input("\nWhat is your Choise :")
        if users_input in options:
            return users_input
        else:
            print("(",users_input,") is invalid option please chose 1,2,3...")

def get_yes_no():
    running_input = input("Continue (y/n):").lower()
    while running_input not in ["y","n"]:
        print("Invalid input. Please enter 'y' or 'n'.")
        running_input = input("Continue? (y/n):").lower()
    if running_input == "y":
        return True
    else:
        return False
def showresult(result):
    print("\nresult =",result,"\n")

def menu():
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    return in_options()

print("CALCULATOR".center(width))
print("\nChoose 1,2,3,4.... based on what mathematical operation you wish to be used")


running = True
while running == True:     #breaks when user inputs 0
    users_input = menu()
    a = float(input("\nfirst number :"))
    b = float(input("\nsecond number :"))
    if users_input == "1":        #main if that deside's what action should be done
        result = op.addition(a,b)
        showresult(result)
    elif users_input == "2":
        result = op.subtraction(a,b)
        showresult(result)
    elif users_input == "3":
        result = op.multiplication(a,b)
        showresult(result)
    elif users_input == "4" and b == 0: #fixes the ZeroDivisionError
        print("\ncant divine with 0")
        continue
    elif users_input == "4":
        result = op.division(a,b)
        showresult(result)

    running = get_yes_no()
print("THANKS!!! for using my CALCULATOR".center(width))
