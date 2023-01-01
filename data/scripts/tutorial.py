import time
import os
from datetime import date
from requests import get, post
from random import randint
from colorama import Fore, Style, init

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

today = date.today()
  
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def tuto():
    print("currently being made....")
    print(bcolors.OKBLUE + "if you want to know how to use the program, open usage.txt")
    time.sleep(5.00)
