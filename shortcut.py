import tkinter as tk
import keyboard
import os
from dotenv import load_dotenv
from PIL import Image
import pystray
import threading

def commands():
    keyboard.add_hotkey("win+t",powershell)
    keyboard.add_abbreviation("email",get_email())

def get_email() -> str:
    return os.getenv("EMAIL")

def powershell():
    return os.startfile("C:/Program Files/PowerShell/7/pwsh.exe")

def on_clicked(icon,item):
    match str(item):
        case "Quit":
            icon.stop()

def icon():
    image = Image.open("kb.ico")
    menu = pystray.Menu(pystray.MenuItem("Quit", on_clicked),)
    icon = pystray.Icon(name="ShorcutApp",icon=image,title="ShorcutApp",menu=menu)
    icon.run()

def main():
    load_dotenv()
    icon_thread = threading.Thread(target=icon)
    commands_thread = threading.Thread(target=commands)
    commands_thread.run()
    icon_thread.run()


main()
