# Fitness booking application using python
'''
1. Classes can be of multiple types - yoga, gym, dance.
2. Each class has a capacity. This refers to the maximum number of users that can attend
the class.
3. Users can book a class if the capacity is not yet reached.
4. If a class is already at capacity, the system should maintain a waiting list of interested
users.
5. Users can cancel the slot upto 30 mins before the class starts. When a user cancels their
booking, allocate the canceled slot to the first user from the waitlist.
'''
from operator import truediv
from time import sleep
import datetime

username_slot_yoga = dict()
waitinglist_slot_yoga = dict()

username_slot_gym = dict()
waitinglist_slot_gym = dict()

username_slot_dance = dict()
waitinglist_slot_dance = dict()

def database_yoga(username, slotno , request, class_name):
    
    if request == 1:
        username_slot_yoga[username].append(class_name+" "+slotno)
        return username_slot_yoga
    if request == 2:
        waitinglist_slot_yoga[username].append(class_name+" "+slotno)
        return waitinglist_slot_yoga
    else:
        return 

    pass

def database_gym(username, slotno , request, class_name):
    
    if request == 1:
        username_slot_gym[username].append(class_name+" "+slotno)
        return username_slot_gym
    if request == 2:
        waitinglist_slot_gym[username].append(class_name+" "+slotno)
        return waitinglist_slot_gym
    else:
        return 

def database_dance(username, slotno , request, class_name):
    
    if request == 1:
        username_slot_dance[username].append(class_name+" "+slotno)
        return username_slot_dance
    if request == 2:
        waitinglist_slot_dance[username].append(class_name+" "+slotno)
        return waitinglist_slot_dance
    else:
        return 

def book_yoga(username, slotno):
    max_capacity = 3   # assuming 3 to be capacity for each slot in classes
    temp = database_yoga(username, slotno, 1, "Yoga")
    
    
    if slotno == 1:

        if len(temp)!= max_capacity:
            print("Booking avaible!")
            print("yoga booked")
            print(database_yoga(username, slotno, 1, "Yoga"))
            
        else:
            database_yoga(username, slotno, 2, "Yoga")

    if slotno == 2:
        if len(temp)!= 3:
            print("Booking avaible!")
            print(database_yoga(username, slotno, 1, "Yoga"))
            
        else:
            database_yoga(username, slotno, 2, "Yoga")

    if slotno == 3:
        if len(temp)!= 3:
            print("Booking avaible!")
            print(database_yoga(username, slotno, 1, "Yoga"))
            
        else:
            database_yoga(username, slotno, 2, "Yoga")

    

def book_gym(username, slotno):
    max_capacity = 3   # assuming 3 to be capacity for each slot in classes
    temp = database_yoga(username, slotno, 1, "Gym")
    if slotno == 1:

        if len(temp)!= max_capacity:
            print("Booking avaible!")
            print("Gym booked")
            print(database_gym(username, slotno, 1, "Gym"))
            
        else:
            database_yoga(username, slotno, 2, "Gym")

    if slotno == 2:
        if len(temp)!= 3:
            print("Booking avaible!")
            print(database_gym(username, slotno, 1, "Gym"))
            
        else:
            database_yoga(username, slotno, 2, "Gym")

    if slotno == 3:
        if len(temp)!= 3:
            print("Booking avaible!")
            print(database_gym(username, slotno, 1, "Gym"))
            
        else:
            database_yoga(username, slotno, 2, "Gym")

def book_dance(username, slotno):
    max_capacity = 3   # assuming 3 to be capacity for each slot in classes
    temp = database_yoga(username, slotno, 1, "Dance")
    if slotno == 1:

        if len(temp)!= max_capacity:
            print("Booking avaible!")
            print("Dancebooked")
            database_gym(username, slotno, 1, "Dance")
            
        else:
            database_yoga(username, slotno, 2, "Dance")

    if slotno == 2:
        if len(temp)!= 3:
            print("Booking avaible!")
            print(database_gym(username, slotno, 1, "Dance"))
            
        else:
            database_yoga(username, slotno, 2, "Dance")

    if slotno == 3:
        if len(temp)!= 3:
            print("Booking avaible!")
            print(database_gym(username, slotno, 1, "Dance"))
            
        else:
            database_yoga(username, slotno, 2, "Dance")
    
    
# GUI for interaction 
# The application contain three slots for booking for the next day for each particular activity

print("Welcome fitness Booking application")
sleep(3)
print()
print(" 1. Yoga")
print(" 2. Gym")
print(" 3. Dance ")
print("Please enter the number in the options to select the type of booking")
n = int(input())
sleep(1)
print("Please Enter username")
username = str(input())

print("Please Select the slots available for tomorrow")
print(" 1. 7:00 AM to 8:00 AM")
print(" 2. 8:00 AM to 9:00 AM")
print(" 3. 9:00 AM to 10:00 AM")
slotno = int(input())

if n == 1:
    book_yoga(username, slotno)
    
if n == 2:
    book_gym(username, slotno)

if n == 3:
    book_dance(username, slotno)

print("thank you for using booking application")






