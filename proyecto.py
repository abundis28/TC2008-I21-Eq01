op1Name = "Example #7"
op2Name = "Example #10"
#TODO(abundis): cambiar a nombre de problema extra
op3Name = "New Example"

def chooseOption():
    print("Enter number of option of code to run:")
    print("1: " + op1Name)
    print("2: " + op2Name)
    print("3: " + op3Name)
    print("4: Exit the program")
    print("")
    option = int(input())
    return option

option = chooseOption()
while option != 4:
    if option == 1:
        print("Running: ", op1Name)
    elif option == 2:
        print("Running: ", op2Name)
    elif option == 3:
        print("Running: ", op3Name)
    elif option != 4:
        print("No option with that number, please try again")
    print("Thanks for running code option: ", option)
    print("")
    option = chooseOption()

print("Thanks for using our program!")
