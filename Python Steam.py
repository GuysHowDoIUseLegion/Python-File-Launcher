import os
import time
import random

os.system("cls")

symbol = "#"
shift = False
LAUNCHER_WINDOW_TITLE = ["Python Steam.py", "Windows PowerShell"]
active = True
root_dir = os.getcwd()
current_dir = os.getcwd()

def load(loading):
    global symbol
    time.sleep(0.3)
    print("Loading [%s%s]" % (symbol * loading, " " * (100 - loading)), end = "\r")
load(5)

while True:
    try:
        import keyboard as key
        load(10)
        break    
    except:
        print("\nKeyboard module not installed; installing", end="\r")
        os.system("pip install keyboard")
        os.system("cls")
        load(10)

while True:
    try:
        import pygetwindow as gw
        load(10)
        break    
    except:
        print("\nPygetwindow module not installed; installing", end="\r")
        os.system("pip install pygetwindow")
        os.system("cls")
        load(10)

apps = []
dirs = []

load(25)

def filesNfolders(current_dir):
    global apps
    global dirs
    global x
    x = 0
    apps = []
    dirs = []
    for file in os.listdir(current_dir):
        if file == "Python Steam.py":
            continue
        
        elif os.path.isfile(os.path.join(current_dir, file)) and list(str(file))[len(file)-1] == "y" and list(str(file))[len(file)-2] == "p" and list(str(file))[len(file)-3] == ".":
            file = file.split(".py")
            del file[1]
            file = "".join(file)
            
            apps.append(file)
        
        #Replace "malware backups here" and "Victims" with any folders you want to exclude
        elif os.path.isdir(os.path.join(current_dir, file)) and file not in ["malware backups here", "Victims"]:
            dirs.append(file)
    
    if apps == []:
        apps = ["None here :("]

    if dirs == []:    
        dirs = ["None here :("]

filesNfolders(current_dir)
        
load(80)

x = 0

def raisex(_):
    global x
    global shift

    if shift == True:
        x += 5
    else:
        x += 1
    listof(x)

load(85)

def lowerx(_):
    global x
    global shift
    if shift == True:
        x -= 5
    else:
        x -= 1
    listof(x)

def shiftOn(_):
    global shift
    if shift == False:
        shift = True

def shiftOff(_):
    global shift
    shift = False

def start(_):
    global x
    global current_dir
    if x < len(dirs) and dirs[x] == "None here :(":
        Shadow_Wizard_Money_Gang = "We love casting spells"
    elif apps[x-len(dirs)] == "None here :(":
        Shadow_Wizard_Money_Gang = "This song is sponsored by the shadow goverment"
    elif x > len(dirs) -1 and current_dir == root_dir:
        os.system(f"start cmd /k python3 \"{current_dir +r"\\" + str(apps[x - len(dirs)])}\".py")
    elif x > len(dirs) - 1 and root_dir != current_dir:
        salt = random.randint(0, 10000)
        target_path = os.path.join(current_dir, ("launcherfile" + str(salt) + ".py"))
        file = apps[x - len(dirs)]
        print(target_path)

        with open(f"{target_path}", "w") as launcher:
            launcher.write('''
import os

os.chdir(r"%s")

os.system(f"start cmd /k python3 \\\"%s\\\".py")
                   
os.remove("%s.py")''' % (current_dir, file, "launcherfile" + str(salt)))
        os.startfile(target_path)
    else:
        current_dir = os.path.join(current_dir, dirs[x])
        filesNfolders(current_dir)
        listof(_)

def cdUp(_):
    global current_dir
    if len(os.path.dirname(current_dir)) < len(root_dir):
        print("Sorry, you don't have permission to access that directory")
        time.sleep(2)
    else:
        current_dir = os.path.dirname(current_dir)
    filesNfolders(current_dir)
    listof(_)

load(90)

def listof(_):
    os.system("cls")
    global current_dir
    print('''
Welcome to Python Steam! To use this program, use the following commands:

    Move up and down with the up and down arrows
        Press shift to move five at a time
          
    Press enter to start a program or enter a folder
          
    Press escape to move up one directory

Current directory: %s

Folders:
''' % current_dir)
    
    global x
    if x > len(apps + dirs) - 1:
        x = len(apps + dirs) -1
    elif x < 0:
        x = 0
    for item in dirs:
        if dirs.index(item) == x:
            extra = "#"
        else:
            extra = " "
        print(extra + " " + item)
    print('''
Apps:
''')
    for item in apps:
        if apps.index(item) + len(dirs) == x:
            extra = "#"
        else:
            extra = " "
        print(extra + " " + item)

def listeners():
    key.on_press_key("down", raisex)
    key.on_press_key("up", lowerx)
    key.on_press_key("shift", shiftOn)
    key.on_release_key("shift", shiftOff)
    key.on_press_key("enter", start)
    key.on_press_key("esc", cdUp)

listeners()

load(100)
time.sleep(1.2)

listof(x)


try:
    while True:
        # Check if the launcher window is focused
        active_window = gw.getActiveWindow()
        if active_window and LAUNCHER_WINDOW_TITLE[0] in active_window.title or active_window and LAUNCHER_WINDOW_TITLE[1] in active_window.title:
            # Activate listeners
            if active == False:
                listeners()
                listof(x)
                active = True
            time.sleep(0.1)
        else:
            # Launcher not focused, stop listener temporarily
            if active == True:
                print("Launcher is not in focus. Stopping listener.")
            key.unhook_all()  # Stop all listeners
            active = False
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")