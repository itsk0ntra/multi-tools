import colorama
from colorama import Fore
import requests
from time import sleep
import os
import os.path
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)

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

def lookup():
    print(bcolors.OKBLUE + """
  _________                                 .____                  __                 
 /   _____/ ______________  __ ___________  |    |    ____   ____ |  | ____ ________  
 \_____  \_/ __ \_  __ \  \/ // __ \_  __ \ |    |   /  _ \ /  _ \|  |/ /  |  \____ \ 
 /        \  ___/|  | \/\   /\  ___/|  | \/ |    |__(  <_> |  <_> )    <|  |  /  |_> >
/_______  /\___  >__|    \_/  \___  >__|    |_______ \____/ \____/|__|_ \____/|   __/ 
        \/     \/                 \/                \/                 \/     |__|    
thanks to https://github.com/cutieQue for making this :]                                      

              Options                                                                 
        """)
    print(bcolors.OKBLUE + """
    [1] Server Invite
    """)
    USER_OPTION = input(    "[>] ")
    if USER_OPTION == "1":
        clearcmd()
        looking_up()

def looking_up():
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{Fore.LIGHTRED_EX}
░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░    ██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗    ██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝    ██║░░░░░██║░░██║██║░░██║█████═╝░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗    ██║░░░░░██║░░██║██║░░██║██╔═██╗░██║░░░██║██╔═══╝░
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║    ███████╗╚█████╔╝╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝    ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░
                                                                    {Fore.LIGHTCYAN_EX}Developed by - Snee
                                                                    https://itssnee.mysellix.io{Fore.RESET}{Fore.LIGHTYELLOW_EX}
""")

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : input(f"\n{Fore.LIGHTYELLOW_EX} Enter Your (user) Token. [>] ")
        }

        guildId = input(f"\n{Fore.LIGHTRED_EX} Enter Guild ID. [>] ")

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        print(f"""{Fore.LIGHTBLUE_EX}
 Guild/Server | Name > {response['name']} 
 Guild/Server | ID > {response['id']}
 Guild/Server | Icon URL > https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
 Guild/Server | Approxomate Amount of Members > {response['approximate_member_count']}
 Guild/Server | Owner > {owner['user']['username']}#{owner['user']['discriminator']} 
 Guild/Server | Owner ID > {response['owner_id']}
 Guild/Server | Region > {response['region']}
""")
        sleep(10)
        exit()
