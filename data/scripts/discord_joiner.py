import sys
import json
import colorama, requests

with open('./config/config.json') as f:
   config = json.load(f)

def joiner():
    invite_code = str(requests.get(config["invite"]).text)
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        tokens = input("Enter the token you want to join a server with: ")
        r1 = requests.get('https://discord.com/api/v10/auth/login', headers={"Authorization": tokens})
        
        if "200" not in str(r1):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Invalid Token")
            
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v10/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
                  
            if "403" in str(r):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Locked Token")
joiner()
