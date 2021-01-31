from threading import Thread, Lock
import threading
import time
import random

############# DECLARATIONS #############

# Interface
op1Name = "Producer - Consumer"
op2Name = "Student rooms"
op3Name = "Sleeping Barber"

# Consumer - Producer
buffer = 0
bufferLock = Lock()

# Student Room
studentsIn = 0
prefectLock = Lock()
studentsLock = Lock()
doorLock = Lock()

# Sleeping Barber
barberLock = Lock()
costumerLock = Lock()
modificationLock = Lock()

############### THREADS ###############

# Consumer - Producer


# Student Room


# Sleeping Barber


######### Execution Functions #########

# Consumer - Producer


# Student Room


# Sleeping Barber


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
