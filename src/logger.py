from pynput import keyboard
class Logger():

    def __init__(self):
        return

    def start(self):
        logger = keyboard.Listener(on_press=self.press)
        logger.start()
        logger.join()

    def press(self, key):
        if key == keyboard.Key.esc:
            print("Exiting...")
            return False
        try:
            char = key.char
            if char.isdigit():
                print(f"Digit Key: {key.char}")
            elif char.isalpha():
                print(f"Character Key: {key.char}")
            elif not char.isalnum():
                print(f"Special Characters: {key.char}")

        except AttributeError:
            print(f"Special Key: {key}")

