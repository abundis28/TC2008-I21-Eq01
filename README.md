# TC2008-I21-Eq01

## Team Members:
  - Andrés Abundis      A01283152
  - Paulina Márquez     
  - Lucas Ortiz         
  - Carlos Madruga      A01283205
  - Adrián Montemayor   A01283139

## Description:
Final project for the class of Operative Systems, this project was made in python, it includes a menu with 4 diferent options, 3 diferent problems and an exit option. When entering on each of the problems, it is asked to the user for how much seconds would they like to run the problem, and is also asked some specific details needed to run the problem, when the time entered by the user is finished, the initial menu will be shown again. 

#### 1) Producer - Consumer:
We have two different concurrent processes and a buffer with two spaces, one of the processes acts as a producer and the other one acts as a consumer.

The processes have some restrictions:

* The producer always produces one item at a time. 
* The comsumer always consumes two items at a time.

#### 2) Student rooms:
We have a room, students and a prefect. We have four processes (students in/out, prefect in/out) and the following restirctions:

* Any student can enter the room with no quantity limit.
* There is only one prefect.
* The prefect can only enter the room if no student is in the room, or if there are 50 or more students in the room at the same time. 
* When the prefect is in the room, no student can get in the room, but if they are already in the room they can leave.
* The prefect cannot get out of the room if there are students in the room. 

#### 3) Sleeping barber:
There is one barber, one barber chair, and n quantity of waiting chairs for the consumers. We have some restrictions:

* If there is no customer, then the barber sleeps in his own chair.
* When a customer arrives, he has to wake up the barber.
* If there are many customers and the barber is cutting a customer’s hair, then the remaining customers either wait if there are empty chairs in the waiting room or they leave if no chairs are empty.

#### Demonstration video: https://youtu.be/GRXgvn25Okg
