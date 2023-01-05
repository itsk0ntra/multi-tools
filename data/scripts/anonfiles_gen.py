#soon will be added
import random, os, requests, json, colorama, time, threading
from colorama import Fore

class console():
  def __init__(self):
        os.system('cls && title Anonfiles Generator ^| github.com/itsstremz ||clear')
  print("""
   _____                       ___________.__.__                 
  /  _  \   ____   ____   ____ \_   _____/|__|  |   ____   ______
 /  /_\  \ /    \ /  _ \ /    \ |    __)  |  |  | _/ __ \ /  ___/
/    |    \   |  (  <_> )   |  \|     \   |  |  |_\  ___/ \___ \ 
\____|__  /___|  /\____/|___|  /\___  /   |__|____/\___  >____  >
        \/     \/            \/     \/                 \/     \/ 
        """)
  Console()  
        
class anon():    
  def  __init__(self):
    self.chars = "abccdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    self.link = ""
    
  def gen(self):
    for i in range(10):
      self.link += random.choice(self.chars)
      self.checker()
      
  def checker(self):
    visit = requests.get(f'https://api.anonfiles.com/v2/file/{self.code}/info').json()
    
    if (visit['status'] == "True"):
      print(f"[{Fore.LIGHTRED_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.GREEN}Working Code: {Fore.WHITE}{r['data']['file']['metadata']['id']}{Fore.RESET}  |  Name: {Fore.WHITE}{self.code}{Fore.RESET}")
            open('./data/output/hits.txt', 'a+').write(f'https://anonfiles.com/{code_id}/{name}\n')
    else:
            print(f"[{Fore.LIGHTRED_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTRED_EX}Invalid Code: {Fore.WHITE}{self.code}{Fore.RESET} | Error: {r['error']['type']}")
        
while True:
    threading.Thread(target=anon().gen()).start()        
