"""

This program is made for random choices,
and all rights is reserved for the creator.
You can not edit or upload this program without the creator's permission,
and if you disobey this, you'll be subject to the full penalty of law.

"""


import sys
import random
import time

class LuckGame_English:

    def help(self):
        return "Add Item : Add | Show List : Show | Pick an Item : Pick | Delete All : Delete | Help : Help | Exit : Exit"

    LuckList = list()

user = LuckGame_English()

while True:
    print(user.help())

    cmd = input("Enter command >> ")
    if cmd == "Add":
        text = input("Enter string to add >> ")
        user.LuckList.append(text)
    elif cmd == "Show":
        print(user.LuckList)
    elif cmd == "Pick":
        pick = random.choice(user.LuckList)
        print("0%")
        time.sleep(random.random())
        print(str(random.randint(1, 11)) + "%")
        time.sleep(random.random())
        print(str(random.randint(12, 22)) + "%")
        time.sleep(random.random())
        print(str(random.randint(23, 33)) + "%")
        time.sleep(random.random())
        print(str(random.randint(34, 44)) + "%")
        time.sleep(random.random())
        print(str(random.randint(45, 55)) + "%")
        time.sleep(random.random())
        print(str(random.randint(56, 66)) + "%")
        time.sleep(random.random())
        print(str(random.randint(67, 77)) + "%")
        time.sleep(random.random())
        print(str(random.randint(78, 88)) + "%")
        time.sleep(random.random())
        print(str(random.randint(89, 99)) + "%")
        time.sleep(random.random())
        print(str(100) + "%" )
        time.sleep(random.random())
        print("The chosen one is...")
        time.sleep(random.random())
        print(pick + "!!")
    elif cmd == "Delete":
        LuckList = []
    elif cmd == "Help":
        print(user.help())
    elif cmd == "Exit":
        sys.exit()
    else:
        print("Please enter command of Add, Show, pick, Delete, Help, Exit.")


#Copyright(c) All Rights Reserved. 2017 Kim DongWoo
