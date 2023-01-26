import os
import ctypes

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def snee():
    clearcmd()
    ctypes.windll.kernel32.SetConsoleTitleW("Snee Grabber | github.com/itssnee")
    print(bcolors.OKBLUE + "it is currently being made...")
    print(bcolors.OKBLUE + "press 1 to go back")
    print(bcolors.OKBLUE + "press 2 to check the grabber status!")
    USER_OPTION = input(bcolors.OKBLUE +    "[>] ")
    if USER_OPTION == "1":
        clearcmd()
        os.system("python main.py")
    elif USER_OPTION == "2":
        clearcmd()
        print("Snee grabber is currently being made...")
        snee()