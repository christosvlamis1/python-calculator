import operations as op
import os

#get the center for aligning later
width = os.get_terminal_size().columns 

#current options upgradeable to a dict when i add more
options = ["1","2","3","4"]

#checks if the users_input is inside options,returns the right input
def in_options():       
    while True:
        users_input = input("\nWhat is your Choice :")
        if users_input in options:
            return users_input
        else:
            print("(",users_input,") is invalid option please chose 1,2,3...")

#Y/N to kill the loop and exit the app
def get_yes_no():                               
    while True:
        running_input = input("Continue? (y/n):").lower()
        if running_input == "y":
            return True
        elif running_input == "n":
            return False

        print("Invalid input. Please enter 'y' or 'n'.")

#prints the result
def showresult(result):
    print("\nresult =",result,"\n")

#gets a float value predicts a ValueError
def get_number(prompt):   
    while True:
        num = input(prompt)
        try:
            num = float(num)
            return num
        except ValueError:
            print("String :("+num+") is an invalid input")

#just a menu print function
def menu():
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")


#main code
print("CALCULATOR".center(width))
print("\nChoose 1,2,3,4.... based on what mathematical operation you wish to be used")

#main while. Handles the give and take
running = True
while running:
    menu() #print menu
    users_input = in_options() #gets the input,validating its on the menu
    
    #prints the name of the operation the user choose
    if users_input == "1":          
        print("\n"+"Addition:".center(width))
    elif users_input == "2":
        print("\n"+"Subtraction:".center(width))
    elif users_input == "3":
        print("\n"+"Multiplication:".center(width))
    elif users_input == "4":
        print("\n"+"Division:".center(width))
    
    #getting our numbers
    num1 = get_number("\nFirst number :")
    num2 = get_number("\nSecond number :")
    
    #deciding what operation to use
    result = None
    if users_input == "1":       
        result = op.addition(num1,num2)
    elif users_input == "2":
        result = op.subtraction(num1,num2)
    elif users_input == "3":
        result = op.multiplication(num1,num2)
    elif users_input == "4":
        #fixes the ZeroDivisionError
        while True:
            num2 =get_number("\nInput any number but 0 :")
            try:
                result = op.division(num1,num2)
                break
            except ZeroDivisionError:
                print("You cannot divine by zero. Try again.")

    #making sure if its an int it doesn't print as float
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    showresult(result)
    running = get_yes_no()
print("THANKS!!! for using my CALCULATOR".center(width))
