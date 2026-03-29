import operations as op
users_input = op.menu() #returns an integer
while users_input != 0:     #breaks when user inputs 0
    a = int(input("\nfirst number :"))
    b = int(input("\nsecond number :"))
    if users_input == 1:        #main if that deside's what action should be done
        result = op.addition(a,b)
        op.showresult(result)
    elif users_input == 2:
        result = op.subtraction(a,b)
        op.showresult(result)
    elif users_input == 3:
        result = op.multiplication(a,b)
        op.showresult(result)
    elif users_input == 4:
        result = op.division(a,b)
        op.showresult(result)
    users_input = op.menu()
print("Thanks for using my calculator")
