import pyperclip
import time

class Clip():
    def __init__(self):
        self.file = "log/clipboard_log.txt"
        return
    
    def start(self):
        value = ""
        while True:
            with open(self.file, "a") as file:
                time.sleep(5)
                curr_value = pyperclip.paste()
                if curr_value != value:
                    value = curr_value
                    print(f"Clipboard Content: {curr_value}")
                    file.write(value + "\n")
                if curr_value == "EXIT":
                    return
