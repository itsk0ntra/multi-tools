from os import access

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


def save2():
    print(bcolors.OKBLUE + """
   _____                                   __      _________                         
  /  _  \   ____  ____  ____  __ __  _____/  |_   /   _____/____ ___  __ ___________ 
 /  /_\  \_/ ___\/ ___\/  _ \|  |  \/    \   __\  \_____  \\__  \\  \/ // __ \_  __ 
/    |    \  \__\  \__(  <_> )  |  /   |  \  |    /        \/ __ \\   /\  ___/|  | \/
\____|__  /\___  >___  >____/|____/|___|  /__|   /_______  (____  /\_/  \___  >__|   
        \/     \/    \/                 \/               \/     \/          \/       
        """)
    print(bcolors.OKBLUE + "since this is currently not working with all the other files, please download it at https://github.com/Vladimir-0001/Discord-account-backup")
