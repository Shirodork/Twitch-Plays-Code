# Import time-based commands
import time

# Keypress package
import pynput

# Windows Direct Keycode input
import ctypes

## Key Codes

########### TO DO ##########
# Add the rest of keyboard #
############################

Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32

LEFT_ARROW = 0x4D
LEFT_ARROW_NUMPAD = 0xCB
RIGHT_ARROW = 0x4B
RIGHT_ARROW_NUMPAD = 0xCD
DOWN_ARROW = 0x50
DOWN_ARROW_NUMPAD = 0xD0
UP_ARROW = 0x48
UP_ARROW_NUMPAD = 0xC8

SPACE = 0x396

SendInput = ctypes.windll.user32.SendInput

def HoldKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def HoldAndReleaseKey(keycode, second):
    HoldKey(keycode)
    time.sleep(second)
    ReleaseKey(keycode)

