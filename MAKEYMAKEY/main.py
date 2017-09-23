from msvcrt import getch
import webbrowser
import subprocess
import sys
new = 2
mariourl = "https://www.learn4good.com/games/maze/kids_online_pcgames.htm"
game = ""

while True:
    key = ord(getch())
    if key == 27: #ESC
        sys.exit()
    elif key == 119: #W
        print("W")
    elif key == 97: #A
        if game == "Mario":
            print("Jump")
        else:
            print("A")
    elif key == 115: #S
        print("S")
    elif key == 100: #D
        print("D")
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            game = "Rolling Cube"
            print("Playing ROLLING CUBE")
            subprocess.Popen([r"C:\Program Files (x86)\SuperJoy\ROLLING CUBE\ROLLING CUBE x86.exe"])
        elif key == 72: #Up arrow
            game = "Mario"
            print("Playing Mario Game")
            webbrowser.open(mariourl, new=new)
        elif key == 75: #Left arrow
            print("Left")
        elif key == 77: #Right arrow
            print("Right")
