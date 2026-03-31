import operations as op
import os

#get the center for aligning later
width = os.get_terminal_size().columns 

#current options upgradeable to a dict when i add more
options = {
    "1": ("Addition", op.addition),
    "2": ("Subtraction", op.subtraction),
    "3": ("Multiplication", op.multiplication),
    "4": ("Division", op.division)
}


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
    for key,value in options.items():
        print(key+"."+value[0])


#main code
print("CALCULATOR".center(width))
print("\nChoose 1,2,3,4.... based on what mathematical operation you wish to be used\n")

#main while. Handles the give and take
running = True
while running:
    menu() #print menu
    users_input = in_options() #gets the input,validating its on the menu
    name , func = options[users_input]
    result = None
    #getting our numbers
    num1 = get_number("\nFirst number :")
    num2 = get_number("\nSecond number :")
    
    #prints the name of the operation the user choose
    print("\n",name.center(width))

    #handling errors like ZerroDivisionError
    while True:
        try:
            result = func(num1, num2)
            break

        #i'm retaking only num2 for now ill change it with more operations than can cause more problems
        except Exception as e:
            print("Invalid input caused :",e,"try again :")
            num2 =get_number("\nInput any number but 0 :")
   
    #making sure if its an int it doesn't print as float
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    showresult(result)
    running = get_yes_no()
print("THANKS!!! for using my CALCULATOR".center(width))
