import random, os, requests, json, colorama, time, threading
from colorama import Fore

class console():
    def __init__(self):
        os.system('cls && title Anonfiles Generator ^| github.com/itsstremz||clear')
        print(f"""
        
   _____                       ___________.__.__                 
  /  _  \   ____   ____   ____ \_   _____/|__|  |   ____   ______
 /  /_\  \ /    \ /  _ \ /    \ |    __)  |  |  | _/ __ \ /  ___/
/    |    \   |  (  <_> )   |  \|     \   |  |  |_\  ___/ \___ \ 
\____|__  /___|  /\____/|___|  /\___  /   |__|____/\___  >____  >
        \/     \/            \/     \/                 \/     \/
                                                     
        github.com/{Fore.RED}itsstremz{Fore.RESET} | github.com/{Fore.RED}itssnee{Fore.RESET} | github.com/{Fore.RED}itssnee/multi-tools{Fore.RESET}      

    """)

console()

class anon():
    def __init__(self):
        self.chars = "abccdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.link = ""
    
    def gen_code(self):
        for i in range(10):
            self.link += random.choice(self.chars)
        self.check()
    
    def check(self):
        r = requests.get(f'https://api.anonfiles.com/v2/file/{self.link}/info').json()

        if(r['status'] == "True"):
            print(f"[{Fore.LIGHTRED_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.GREEN}Working Code: {Fore.WHITE}{r['data']['file']['metadata']['id']}{Fore.RESET}  |  Name: {Fore.WHITE}{self.link}{Fore.RESET}")
            open('good_code.txt', 'a+').write(f'https://anonfiles.com/{code_id}/{name}\n')
        else:
            print(f"[{Fore.LIGHTRED_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTRED_EX}Invalid Code: {Fore.WHITE}{self.link}{Fore.RESET} | Error: {r['error']['type']}")
            
while True:
    threading.Thread(target=anon().gen_code()).start()
    threading.Thread(target=anon().gen_code()).start()
