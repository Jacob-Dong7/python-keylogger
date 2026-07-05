from src.logger import Logger
from src.clipboard_logger import Clip
def main():
    while True:
        print("=" * 100)
        print("KEY LOGGER")
        print("=" * 100)
        print("[-1] Exit [1] Keylogger [2] Clipboard Logger [3] Clear Key Log [4] Clear Clipboard Log [5] Instructions")
        print("=" * 100)
        option = input("Select: ")
        print("-" * 100)
        if option == "1":
            logger = Logger()
            logger.start()
        elif option == "2":
            logger = Clip()
            logger.start()
        elif option == "-1":
            print("Exiting...")
            return
        elif option == "3":
            with open("log/log.txt", "w") as file:
                file.write("")
                print("Key Log Cleared")
                file.close()
        elif option == "4":
            with open("log/clipboard_log.txt", "w") as file:
                file.write("")
                print("Clipboard Log Cleared")
                file.close()
        elif option == "5":
            print("INSTRUCTIONS:")
            print("For key logger, press 'esc' to exit")
            print("For clipboard logger, copy and paste the word 'EXIT' to exit")
        else:
            print("WARNING:")
            print("Please select from the available options")


if __name__ == "__main__":
    main()