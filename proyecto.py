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
def ProducerThread():
    global buffer
    while True:
        if buffer < 2:
            bufferLock.acquire()
            buffer += 1
            print("Produced data:", buffer)
            bufferLock.release()
            time.sleep(random.random())
        if stopThreadsCP:
            break

def ConsumerThread():
    global buffer
    while True:
        if buffer == 2:
            bufferLock.acquire()
            buffer = 0
            print("Consumed data. Remaining: ", buffer)
            bufferLock.release()
            time.sleep(random.random())
        if stopThreadsCP:
            break

# Student Room
def PrefectIn():
    global studentsIn
    while True:
        if (studentsIn > 50 or studentsIn == 0) and not prefectLock.locked() and not doorLock.locked():
            doorLock.acquire()
            print("Prefect in Room")
            prefectLock.acquire()
            doorLock.release()
            time.sleep(random.random())
        if stopThreadsSR:
            break

def PrefectOut():
    global studentsIn
    while True:
        if studentsIn == 0 and prefectLock.locked() and not doorLock.locked():
            doorLock.acquire()
            print("Prefect left Room")
            prefectLock.release()
            doorLock.release()
            time.sleep(random.random())
        if stopThreadsSR:
            break

def StudentOut():
    global studentsIn
    while True:
        if studentsIn > 0 and not doorLock.locked():
            doorLock.acquire()
            studentsLock.acquire()
            studentsIn -= 1
            print("A student left. Students left in the room:", studentsIn)
            studentsLock.release()
            doorLock.release()
            time.sleep(random.random())
        if stopThreadsSR:
            break

def StudentIn():
    global studentsIn
    while True:
        if not prefectLock.locked() and not doorLock.locked():
            doorLock.acquire()
            studentsLock.acquire()
            studentsIn += 1
            print("A student entered. Students in the room:", studentsIn)
            studentsLock.release()
            doorLock.release()
            time.sleep(random.random())
        if stopThreadsSR:
            break

# Sleeping Barber


######### INTERFACE (MAIN) #########
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
        print("")
        stopThreadsCP = False
        producer = threading.Thread(target=ProducerThread)
        consumer = threading.Thread(target=ConsumerThread)
        timeCP = int(input("Time for the program to run: "))
        print("")
        print("--- Buffer size: 2")
        producer.start()
        consumer.start()
        time.sleep(timeCP)
        print("-- Stopping threads --")
        stopThreadsCP = True
        producer.join()
        consumer.join()
    elif option == 2:
        print("Running: ", op2Name)
        print("")
        stopThreadsSR = False
        pI = threading.Thread(target=PrefectIn)
        pO = threading.Thread(target=PrefectOut)
        sI = threading.Thread(target=StudentIn)
        sO = threading.Thread(target=StudentOut)
        timeSR = int(input("Time for the program to run: "))
        print("")
        print("--- Room capacity: 50 students")
        pI.start()
        pO.start()
        sI.start()
        sO.start()
        time.sleep(timeSR)
        stopThreadsSR = True
        pI.join()
        pO.join()
        sI.join()
        sO.join()
    elif option == 3:
        print("Running: ", op3Name)
    elif option != 4:
        print("No option with that number, please try again")
    print("")
    print("Thanks for running code option: ", option)
    print("")
    option = chooseOption()

print("Thanks for using our program!")
