import pyperclip
import time

class Clip():
    def __init__(self):
        return
    
    def start(self):
        value = ""
        while True:
            time.sleep(5)
            curr_value = pyperclip.paste()
            if curr_value != value:
                value = curr_value
                print(curr_value)
            if curr_value == "EXIT":
                return
