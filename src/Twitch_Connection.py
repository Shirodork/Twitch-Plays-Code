# Python system libraries
import sys
# Package that allows us to open a connection to Twitch
import socket
# Random generation (like numbers) 
import random
# Regular Expressions (ReGEX)
import re

# New Class
class Twitch:
    

    def connect_twitch(self, channel):

        # Defining a "channel" variable
        self.channel = channel

        # Create a socket
        print('Establishing Connection to Twitch')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the Socket
        print('Connecting to Socket')
        self.sock.connect(('irc.chat.twitch.tv', 6667))

        # Pass account deets anonymously (Google JustinFan)
        print('Connestion Established. Logging Into Twitch')
        user = 'justinfan%i' % random.randint(1000, 99999)
        self.sock.send(('PASS 1234\r\nNICK %s\r\n' % user).encode())
        print('Login successful. Joining Channel: %s' % self.channel)
        self.sock.send(('JOIN #%s\r\n' % self.channel).encode())
        print('Successfully Connected to Twitch Channel: %s' % self.channel)

    # Handle Reconnect
    def reconnect(self):
        self.connect_twitch(self.channel)

    # Checks to see if message is a chat message and not some kind of event message
    def is_chat_message(self, chatdata):
        return re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv) PRIVMSG #[a-zA-Z0-9_]+ :.+$', chatdata)

    # Split the message into parts
    def parse_message(self, chatdata):
        return {
            'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', chatdata)[0],
            'message': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', chatdata)[0]
        }

    # Grabs twitch messages from the socket
    def twitch_get_messages(self):

        # Var to hold chat data
        chatdata = None

        # Receive Messages from Socket
        try: chatdata = self.sock.recv(2048).decode()
        except: return False

        # print(chatdata)

        # Check see if were recieving data. If no data, reconnect
        if not chatdata:
            print('No Data Recieved. Reconnecting...')
            self.reconnect()
            return None

        #Debug
        #print("Debug: " + chatdata)


        # Filter chat messages and filter/split into array
        if self.is_chat_message(chatdata):
            return [self.parse_message(line) for line in filter(None, chatdata.split('\r\n'))]
        #else: return ('[Message Filtered]')