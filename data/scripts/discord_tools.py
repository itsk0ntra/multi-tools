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
from data.scripts.discord_lookup import lookup

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

def dc_tools():
    print(bcolors.OKBLUE + """
________  .__                              .___ ___________           .__          
\______ \ |__| ______ ____  ___________  __| _/ \__    ___/___   ____ |  |   ______
 |    |  \|  |/  ___// ___\/  _ \_  __ \/ __ |    |    | /  _ \ /  _ \|  |  /  ___/
 |    `   \  |\___ \\  \__(  <_> )  | \/ /_/ |    |    |(  <_> |  <_> )  |__\___ \ 
/_______  /__/____  >\___  >____/|__|  \____ |    |____| \____/ \____/|____/____  >
        \/        \/     \/                 \/                                  \/ 
                                      

              Options                                                                 
        """)
    print(bcolors.OKBLUE + """
    [1] Discord Token Checker
    [2] (Bot Account Only) Discord Server Nuker
    [3] Discord Server ID Lookup
    [4] Mass DM
    [5] Back
    [6] Quit
    """)
    USER_OPTION = input(    "[>] ")
    if USER_OPTION == "1":
        clearcmd()
        os.system('python ./data/scripts/discord_checker.py')  
    elif USER_OPTION == "2":
        clearcmd()
        os.system('python ./data/scripts/discord_nuker.py')
    elif USER_OPTION == "3":
        clearcmd()
        lookup()
    elif USER_OPTION == "4":
        clearcmd()
        os.system('python ./data/scripts/discord_joiner.py')
    elif USER_OPTION == "6":
        clearcmd()
        os.system("python main.py")
    elif USER_OPTION == "7":
        quit()
    elif USER_OPTION == "5":
        clearcmd()
        save2()
