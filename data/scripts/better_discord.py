import time
import os
from datetime import date
from requests import get, post
from random import randint
from colorama import Fore, Style, init
import webbrowser

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

def better_dc():
    print(bcolors.OKBLUE + """
__________        __    __                 ________  .__                              .___
\______   \ _____/  |__/  |_  ___________  \______ \ |__| ______ ____  ___________  __| _/
 |    |  _// __ \   __\   __\/ __ \_  __ \  |    |  \|  |/  ___// ___\/  _ \_  __ \/ __ | 
 |    |   \  ___/|  |  |  | \  ___/|  | \/  |    `   \  |\___ \\  \__(  <_> )  | \/ /_/ | 
 |______  /\___  >__|  |__|  \___  >__|    /_______  /__/____  >\___  >____/|__|  \____ | 
        \/     \/                \/                \/        \/     \/                 \/ 
                                      

              Options                                                                 
        """)
    print(bcolors.OKBLUE + """
    [1] Recommended Themes
    [2] Recommended Plugins
    [3] Quit
    """)
    USER_OPTION = input(bcolors.OKBLUE +     "[>] ")
    if USER_OPTION == "1":
        clearcmd()
        webbrowser.open('https://github.com/mwittrien/BetterDiscordAddons/tree/master/Themes')
        time.sleep(2.00)
        better_dc()
    elif USER_OPTION == "2":
        clearcmd()
        webbrowser.open('https://github.com/mwittrien/BetterDiscordAddons/tree/master/Plugins')
        time.sleep(2.00)
        better_dc()
    elif USER_OPTION == "3":
        clearcmd()
        print(bcolors.OKBLUE + """
        ________        .__  __    __  .__                
        \_____  \  __ __|__|/  |__/  |_|__| ____    ____  
        /  / \  \|  |  \  \   __\   __\  |/    \  / ___\ 
       /   \_/.  \  |  /  ||  |  |  | |  |   |  \/ /_/  /
       \_____\ \_/____/|__||__|  |__| |__|___|  /\___  / 
              \__/                            \//_____/  
       """)
        time.sleep(2.00)
