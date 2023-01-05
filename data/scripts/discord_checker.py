import os
import time
from requests import get, post
from random import randint

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

choice = input("do you want to use proxies?(y/n)")
if choice == "y":
    clearcmd()
    os.system('python ./data/scripts/proxy_checker.py')
elif choice == "n":
    clearcmd()
else:
    print("invalid answer!")
    time.sleep(2.00)
    os.system('python ./data/scripts/discord_checker.py')
    
def variant1(token):
    with open('./config/tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                response = post(f'https://discord.com/api/v6/invite/QCSBmWX3Me', headers={'Authorization': token},)
                if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
                    return False
                else:
                    return True

def variant1_Status(token):
    response = post(f'https://discord.com/api/v6/invite/QCSBmWX3Me', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('./config/tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant1(token) == True:
                    print(f'Token: {token} is Valid')
                    checked.append(token)
                else:
                    print(f'Token: {token} is Invalid')
        if len(checked) > 0:
            save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
            if save == 'y':
                name = "working_tokens"
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
        input('Press Enter For Exit...')
    except:
        input('Can`t Open "tokens.txt" File! Press enter to close the program...')
