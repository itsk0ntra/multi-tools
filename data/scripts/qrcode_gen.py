import qrcode
import time

print("https://github.com/itssnee/ on top")
print("""
________ __________  _________            .___          ________               
\_____  \\______   \ \_   ___ \  ____   __| _/____     /  _____/  ____   ____  
 /  / \  \|       _/ /    \  \/ /  _ \ / __ |/ __ \   /   \  ____/ __ \ /    \ 
/   \_/.  \    |   \ \     \___(  <_> ) /_/ \  ___/   \    \_\  \  ___/|   |  
\_____\ \_/____|_  /  \______  /\____/\____ |\___  >   \______  /\___  >___|  /
       \__>      \/          \/            \/    \/           \/     \/     \/ 
       """)

data = input("Enter your link:")
img = qrcode.make(data)
img.save('QRCode.png')
print("saved qr code as QRCode.png in this folder.")
print("if you enjoyed the program, please give it a star on github.")
time.sleep(5.00)
