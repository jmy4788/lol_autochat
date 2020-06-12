from eng2kor import kor2eng
from lolAPI import writedata
from keyboard_input import keyboard_input, AltTab
import win32com.client as win32
import win32gui
import win32con
import sys
import time


def name_insert(input_text):
    output_text = input_text.replace("{name}", name)
    return output_text


def find_window(s_app_name):

    try:
        hwnd = win32gui.FindWindow(None, s_app_name)
        return hwnd
    except gui_err:
        pass

    try:
        hwnd = FindWindow(s_app_name, None)
        return hwnd
    except gui_err:
        return None


if __name__ == "__main__":
    app_name = 'RiotWindowClass'
    writedata('정민영v')

    hwnd = win32gui.FindWindow(app_name, None)
    if hwnd is None:
        print("%r has no window." % app_name)
        input('press enter to close')
        exit()

    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, 9)
    time.sleep(0.5)

    f_1 = open("textdata.py", 'r', encoding='UTF-8')
    lines = f_1.readlines()

    for line in lines:
        line_2 = kor2eng(line)
        keyboard_input(line_2)

f_1.close()
exit()