import requests
import random
from requests import get

def variant1(token):
    s = requests.session()
    proxy = set()

    with open('./config/proxies.txt', 'r') as f:
        file_lines1 = f.readlines()
        for line1 in file_lines1:
            proxy.add(line1.strip())

    proxies = {
        'http': 'http://'+random.choice(list(proxy))
    }
    with open('./config/tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                
                response = get(f'https://discord.com/api/v6/invite/QCSBmWX3Me', headers={'Authorization': token}, proxies=proxies)
                if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
                    return False
                else:
                    return True

def variant1_Status(token):
    s = requests.session()
    proxy = set()
    with open('./config/proxies.txt', 'r') as e:
        file_lines1 = e.readlines()
        for line1 in file_lines1:
            proxy.add(line1.strip())
    proxies = {
        'http': 'http://'+random.choice(list(proxy))
    }
    response = get(f'https://discord.com/api/v6/invite/QCSBmWX3Me', headers={'Authorization': token}, proxies=proxies)
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
