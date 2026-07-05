from src.logger import Logger
from src.clipboard_logger import Clip
def main():
    while True:
        print("[-1] Exit [1] Keylogger [2] Clipboard Logger")
        option = input("Select: ")
        if option == "1":
            logger = Logger()
            logger.start()
        elif option == "2":
            logger = Clip()
            logger.start()
        elif option == "-1":
            print("Exiting...")
            return

if __name__ == "__main__":
    main()
