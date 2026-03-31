import operations as op
import os

#get the center for aligning later
width = os.get_terminal_size().columns 


def show_history():
    if not history:
        os.system("clear")
        print("\nHistory is empty\n")
        input("Press Enter to return to menu...\n")
        os.system("clear")
    else:
        os.system("clear")
        for index, item in enumerate(history):
            print("\n"+str(index+1)+".  "+item)
        input("Press Enter to return to menu...\n")
        os.system("clear")

#checks if the users_input is inside options,returns the right input
def in_options():       
    while True:
        users_input = input("\nWhat is your Choice :").lower()
        if users_input in options:
            return users_input
        else:
            print("(",users_input,") is invalid option please choose 1,2,3...")

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


options = {
    "1": ("Addition", op.addition, "+"),
    "2": ("Subtraction", op.subtraction, "-"),
    "3": ("Multiplication", op.multiplication, "*"),
    "4": ("Division", op.division, "/"),
    "h": ("History", show_history, None)
}

history = []


#main code
print("CALCULATOR".center(width))
print("\nChoose 1,2,3,4.... based on what mathematical operation you wish to be used\n")
print("Press H to view history")

#main while. Handles the give and take
running = True
while running:
    menu() #print menu
    users_input = in_options()#gets the input,validating its on the menu
    name , func , symbol = options[users_input]
    if symbol is None:
        func()
        continue
    else:
        #getting our numbers
        num1 = get_number("\nFirst number :")
        num2 = get_number("\nSecond number :")
        
        #prints the name of the operation the user choose
        print("\n",name.center(width))

        #handling errors like ZeroDivisionError
        while True:
            try:
                result = func(num1, num2)
                break

            #i'm retaking only num2 for now ill change it with more operations that can cause more problems
            except Exception as e:
                print("Invalid input caused :",e,"try again :")
                num2 =get_number("\nInput any number but 0 :")
       
        #making sure if its an int it doesn't print as float
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        if num1.is_integer():
            num1 = int(num1)
        if num2.is_integer():
            num2 = int(num2)
        result_log = str(num1)+" "+symbol+" "+str(num2)+" = "+str(result)
        if len(history) >= 10:
            history.pop(0)
            history.append(result_log)
        else:
            history.append(result_log)

        showresult(result)
        running = get_yes_no()
print("THANKS!!! for using my CALCULATOR".center(width))
