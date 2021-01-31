from threading import Thread, Lock
import threading
import time
import random

############# DECLARATIONS #############
##### Interface
op1Name = "Producer - Consumer"
op2Name = "Student rooms"
op3Name = "Sleeping Barber"

##### Consumer - Producer
bufferLock = Lock()

##### Student Room
prefectLock = Lock()
studentsLock = Lock()
doorLock = Lock()

##### Sleeping Barber
barberLock = Lock()
costumerLock = Lock()
modificationLock = Lock()

############### THREADS ###############
##### Consumer - Producer
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

##### Student Room
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

##### Sleeping Barber
def Barber():
    global freeSeats
    while True:
        if costumerLock.locked():
            if not modificationLock.locked():
                modificationLock.acquire()
                barberLock.acquire()
                freeSeats += 1
                print("Barber: Cutting hair // Free seats: ", freeSeats)
                if freeSeats == seats:
                    costumerLock.release()
                barberLock.release()
                modificationLock.release()
        else:
            print("Barber: No costumers waiting")
        time.sleep(random.random())
        if stopThreadsSP:
            break


def Customer():
    global freeSeats
    while True:
        if not modificationLock.locked():
            modificationLock.acquire()
            if freeSeats > 0:
                freeSeats -= 1
                print("Costumer: Sit, hello // Free seats", freeSeats)
                if not costumerLock.locked():
                    costumerLock.acquire()
            else:
                print("Costumer: No seats available, bye")
            modificationLock.release()
            time.sleep(random.random())
            if stopThreadsSP:
                break

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
        buffer = 0
        stopThreadsCP = False
        producer = threading.Thread(target=ProducerThread)
        consumer = threading.Thread(target=ConsumerThread)
        timeCP = int(input("Type the number of seconds the option will run: "))
        print("")
        print("--- Buffer size: 2")
        producer.start()
        consumer.start()
        time.sleep(timeCP)
        print("-- Time limit reached: stopping threads --")
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
        timeSR = int(input("Type the number of seconds the option will run: "))
        print("")
        print("--- Room capacity: 50 students")
        studentsIn = int(input("Number of students already inside of room: "))
        print("")
        pI.start()
        pO.start()
        sI.start()
        sO.start()
        time.sleep(timeSR)
        print("-- Time limit reached: stopping threads --")
        stopThreadsSR = True
        pI.join()
        pO.join()
        sI.join()
        sO.join()
    elif option == 3:
        print("Running: ", op3Name)
        print("")
        stopThreadsSP = False
        barb = threading.Thread(target=Barber)
        cons = threading.Thread(target=Customer)
        timeSP = int(input("Type the number of seconds the option will run: "))
        print("")
        seats = int(input("Type number of seats in the barbershop: "))
        print("")
        freeSeats = seats
        barb.start()
        cons.start()
        time.sleep(timeSP)
        print("-- Time limit reached: stopping threads --")
        stopThreadsSP = True
        barb.join()
        cons.join()
    if option > 4 or option < 1:
        print("No option with that number, please try again")
    else:
        print("")
        print("Thanks for running code option: ", option)
    print("")
    option = chooseOption()

print("Thanks for using our program!")
