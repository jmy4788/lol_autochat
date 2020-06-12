import ctypes
import time
from ctypes import wintypes
user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.Microsoft.com/en-us/library/dd375731

CHARACTER_UPPER = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
CHARACTER_LOWER = list('abcdefghijklmnopqrstuvwxyz')
CHARACTER_NUMBER = list('1234567890-=')
CHARACTER_SPECIAL = list('!@#$%^&*())_+')

HEX_CODE = [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50,
           0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A]
HEX_CODE_NUM = [0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0xBD, 0xBB]
CHARACTER_HEX_UPPER = dict(zip(CHARACTER_UPPER, HEX_CODE))
CHARACTER_HEX_LOWER = dict(zip(CHARACTER_LOWER, HEX_CODE))
CHARACTER_HEX_NUMBER = dict(zip(CHARACTER_NUMBER, HEX_CODE_NUM))
CHARACTER_HEX_SPECIAL = dict(zip(CHARACTER_SPECIAL, HEX_CODE_NUM))

VK_ENTER = 0x0D
VK_TAB  = 0x09
VK_MENU = 0x12
VK_HANYEONG = 0x15
VK_T = 0x54
VK_K = 0x4B
VK_F = 0x46
VK_D = 0x44
VK_G = 0x47
VK_O = 0x4F

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)


def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args


user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions


def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def AltTab():
    """Press Alt+Tab and hold Alt key for 2 seconds
    in order to see the overlay.
    """
    PressKey(VK_MENU)   # Alt
    PressKey(VK_TAB)    # Tab
    ReleaseKey(VK_TAB)  # Tab~
    time.sleep(0.1)
    ReleaseKey(VK_MENU) # Alt~


def keyboard_input(text):
    count = 0
    PressKey(0x10)
    PressKey(0x0D)
    ReleaseKey(0x10)
    ReleaseKey(0x0D)
    time.sleep(0.01)
    Han_Flag = False

    for b in text[0]:
        if text[1][count] and not Han_Flag:
            time.sleep(0.01)
            PressKey(VK_HANYEONG)
            ReleaseKey(VK_HANYEONG)
            Han_Flag = True
        elif not text[1][count] and Han_Flag:
            time.sleep(0.01)
            PressKey(VK_HANYEONG)
            ReleaseKey(VK_HANYEONG)
            Han_Flag = False
        for c in b:
            if c.isupper():
                PressKey(0x10)#0x10 Shift
                PressKey(CHARACTER_HEX_UPPER[c])
                ReleaseKey(CHARACTER_HEX_UPPER[c])
                ReleaseKey(0x10)
            elif c.islower():
                PressKey(CHARACTER_HEX_LOWER[c])
                ReleaseKey(CHARACTER_HEX_LOWER[c])
            elif any(a in c for a in '1234567890-='):
                PressKey(CHARACTER_HEX_NUMBER[c])
                ReleaseKey(CHARACTER_HEX_NUMBER[c])
            elif any(a in c for a in '!@#$%^&*()_+'):
                PressKey(0x10)  # 0x10 Shift
                PressKey(CHARACTER_HEX_SPECIAL[c])
                ReleaseKey(0x10)
                ReleaseKey(CHARACTER_HEX_SPECIAL[c])
            elif c.isspace():
                PressKey(0x20)  # 0x20 Space
                ReleaseKey(0x20)
        count += 1
        time.sleep(0.002)
    PressKey(0x0D)
    ReleaseKey(0x0D)
    time.sleep(0.01)
    return


if __name__ == "__main__":
    AltTab()
    time.sleep(1)


"""    

"""