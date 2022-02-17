# Twitch-Plays-Code
A Twitch Plays Code. Connect to your channel and play! 

# Code Structure
### Twitch_Connection.py
This code handles the connection to Twitch. You should not need to edit this code at all! Logs into a twitch channel anonymously using JustinFan### account generation

### Twitch_Control.py
The main code used to define inputs and your channel. A few things to do here:

##### Define your channel! 
TWITCH_CHANNEL = 'enterchannelhere'    # Define the twitch channel [ Replace with you twitch channel in lowercase ]

Within the Twitch_Control.py script, there is this variable. Change the 'enterchannelhere' part with your channel name (in lowercase letters). 

Example: TWITCH_CHANNEL = 'xqcow'

##### Define Commands

There will be a section where you can define commands. There are three different types of commands you can use:
###### HoldAndReleaseKey()
>> This will let you define a key to hold and a time to hold it! Follow this syntax:
>> HoldAndReleaseKey(W, 2) ## This will hold the W key for 2 second
>> You can find a list of useable keys in the Twitch_KeyCommands.py script!

###### HoldKey()
>> This will hold the key indefinitely. Define the key only
>> Example: HoldKey(w) ## This will hold the W key

######ReleaseKey
>> This will Release any previously held Key. Use in conjunction with the HoldKey() function
>> Example: ReleaseKey(w) ## This will release the W key

### Twitch_KeyCommands.py
This script holds all the available key commands you can program. I will update this with the full keyboard soon. 
