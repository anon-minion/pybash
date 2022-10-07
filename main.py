import os.path
import csv
from colorama import init, Fore, Back
import time
from gopy import golib



deprecated = {"dir" : "ls", "cls" : "clear"}

try:
    while True:
       
        print(os.getcwd(), end="")
       
        command = input("> ")
   
        if command.lower() == "ls":
            os.system("dir")
        elif command.lower() == "clear":
            os.system("cls")
        elif command.lower() == "test":
            os.chdir("C:/Users/ICS")
        elif "cd" in command.lower():
            new_str = command.removeprefix("cd ")
            try:
                c = os.getcwd()
                if "\\" in c:
                     new = c.replace("\\", "/")
            
                full_text = f"{new}/{new_str}"
                os.chdir(full_text)
            
            except Exception as err:
                print("WinError")
        elif "isthispython" in command.lower():
            print("yes this is python")
        elif command.lower() == "man":
            pass
        elif command.lower() == "bash":
            print("PyBash version 0.1 ---")
        elif command.lower() in deprecated.keys():
            print("This is not a valid Bash Command But a Batch Command")
            print("use ", deprecated[command], " instead")
        elif golib.has_prefix(command.lower(), "winrun"):
            split = command.removeprefix("winrun ")
            os.system(split)
        else:
            print("Not a Valid Bash Command")
except Exception as M:
    print("Internal Problem-- Please Headover to minions.org for help")