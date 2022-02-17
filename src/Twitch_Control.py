#############################################
### Required Packages (Dont need to edit) ###
#############################################

# I dont remember adding this lol
from hashlib import new
# Import Twitch_Connection.py script
import Twitch_Connection
# Import Keyboard package
import keyboard
# Import Twitch Key Commands Script
from Twitch_KeyCommands import *
# Import The Parallel processing code
import concurrent.futures
# Import the Time package
import time

######################################################################################
### DEFINE VARIABLES HERE - FEEL FREE TO EDIT THIS SECTION BASED ON WHAT YOU NEEED ###
######################################################################################

TWITCH_CHANNEL = 'channelnamehere'    # Define the twitch channel [ Replace with you twitch channel in lowercase ]

MAX_WORKERS = 5    # Defining how many processes we want to run at the same time
MESSAGE_RATE = 1    # How fast we want to process messages (MUST BE between 0-1)

message_queue = []  # Messages in the queue
active_queue = []   # Active messages to be handled
worker_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)    # Defining amount of Threads
last_message_time = time.time() # When the last mesasge came in

#####################
### Start of Code ###
#####################

# Initiate connection to Twitch
t = Twitch_Connection.Twitch()      # Assigns Twitch Connection Class to "t"
t.connect_twitch(TWITCH_CHANNEL)    # Connect to the channel defined

###########################################
### Define Countdown before Code Starts ###
###########################################

COUNTDOWN = 5
while COUNTDOWN > 0:
    print(COUNTDOWN)
    COUNTDOWN -= 1
    time.sleep(1)

############################
### Define Commands Here ###
############################

# Function to handle Messages and Keypresses
def press_buttons(msg):

    msg = mtest['message'].lower()            # Filter Message. Convert to lowercase
    username = mtest['username'].lower()      # Filter Username. Convert to lowercase

    # Debug - Print
    print(username + ": " + msg)

    ## Message Filter 
    if msg == "short left":
        HoldAndReleaseKey(LEFT_ARROW_NUMPAD, .75)

    if msg == "left":
        HoldAndReleaseKey(LEFT_ARROW_NUMPAD, 2)

    if msg == "short right":
        HoldAndReleaseKey(RIGHT_ARROW_NUMPAD, .75)
    
    if msg == "right":
        HoldAndReleaseKey(RIGHT_ARROW_NUMPAD, 2)

    if msg == "yeet right":
        HoldAndReleaseKey(RIGHT_ARROW_NUMPAD, 5)
    
    if msg == "yeet left":
        HoldAndReleaseKey(LEFT_ARROW_NUMPAD, 5)

    if msg == "up":
        HoldAndReleaseKey(UP_ARROW_NUMPAD, 2)

    if msg == "down":
        HoldAndReleaseKey(DOWN_ARROW_NUMPAD, 2)

    if msg == "jump":
        HoldAndReleaseKey(C, 2)

    if msg == "rump":
        HoldKey(RIGHT_ARROW_NUMPAD)
        HoldKey(C)
        time.sleep(.8)
        ReleaseKey(RIGHT_ARROW_NUMPAD)
        ReleaseKey(C)

    if msg == "lump":
        HoldKey(LEFT_ARROW_NUMPAD)
        HoldKey(C)
        time.sleep(.8)
        ReleaseKey(LEFT_ARROW_NUMPAD)
        ReleaseKey(C)

    if msg == "twirl":
        HoldAndReleaseKey(V, 2)
    
    if msg == "start":
        HoldAndReleaseKey(SPACE, 2)

    if msg == "b":
        HoldAndReleaseKey(C, 2)

    if msg == "a":
        HoldAndReleaseKey(V, 2)

    if msg == "x":
        HoldAndReleaseKey(D, 2)

    if msg == "y":
        HoldAndReleaseKey(X, 2)


# Main Function Loop
while True:

    # Set the Active Queue to "be active"
    active_queue = [t for t in active_queue if not t.done()]

    # Add New incomming messages to the message_queue array
    new_messages = t.twitch_get_messages()  # Gather Messages

    # If there are new messages
    if new_messages:
        message_queue += new_messages   # Add the new message to the end of the queue
    
    # Hold the messages that we want to handle before executing
    messages_to_handle = []
    
    # Determine how many messages to handle
    if not message_queue:   # If there are no new messages
        last_message_time = time.time() # Track the last mess
    else:   # If there ARE messages
        
        mRate = MESSAGE_RATE

        # mRate = 1 if MESSAGE_RATE == 0 else ( time.time() - last_message_time ) / MESSAGE_RATE     # Determine  how many messages we want to proccess
        mAmount = int(mRate * len(message_queue))       # Determine how many actual messages get processed
        
        ## Debug
        print(mAmount)
        print(message_queue[0])

        # if we have messages to process
        if mAmount > 0:
            messages_to_handle = message_queue[0:mAmount]   # Take that amount of messages from the queue
            del message_queue[0:mAmount]                    # Delete those processed messages from the queue
            last_message_time = time.time()                 # Mark the time
            
    '''
    try keyboard.is_pressed('backspace+shift'):
        exit()

    except Exception as e

    '''
    # If there are NOT messages from chat that we want to handle...
    if not messages_to_handle:
        # Break the if/else and continue the loop
        continue    
    else:   # If there ARE messages to handle
            # For every message in the new queue
        for mtest in messages_to_handle:
                # Check to see if there are enough workers to handle the messages
            if len(active_queue) <= MAX_WORKERS:
                active_queue.append(worker_pool.submit(press_buttons, mtest)) # Pass messages to workers along with the (Press buttons) function
            # If there are NOT enough workers
            else:
                print("HEY DUM DUM. INCREASE MAX WORKERS. YOU GOT TOO MANY MESSAGES COMING IN!")    # Tell strimmer to add more workers to code, otherwise there will be missed messages



    '''
    # End script (WIP BROKEN)
    if keyboard.is_pressed('space'):
        exit()

    # Gather Messages
    new_messages = t.twitch_get_messages()

    # Checks to see if there are messages
    if not new_messages:
        # If theres no messages
        continue
    else:
        # for every message, split into username and message vars
        for message in new_messages:
            msg = message['message'].lower()            # Filter Message. Convert to lowercase
            username = message['username'].lower()      # Filter Username. Convert to lowercase

            # Debug - Print
            print(username + ": " + msg)

            press_buttons(msg)

    '''


    