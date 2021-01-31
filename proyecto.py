from threading import Thread, Lock
import threading
import time
import random

####### INTERFACE DECLARATIONS
op1Name = "Producer - Consumer"
op2Name = "Student rooms"
op3Name = "Sleeping Barber"

####### CONSUMER-PRODUCER DECLARATIONS
buffer = 0
bufferLock = Lock()

####### STUDENT ROOM DECLARATIONS
studentsIn = 0
prefectLock = Lock()
studentsLock = Lock()
doorLock = Lock()

####### SLEEPING BARBER DECLARATIONS
barberLock = Lock()
costumerLock = Lock()
modificationLock = Lock()

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
