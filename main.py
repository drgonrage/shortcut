# import tkinter as tk
from dotenv import load_dotenv
import keyboard
import os

load_dotenv()

class ShortCutApp:
    def __init__(self) -> None:
        self.__email = os.getenv("EMAIL")
        self.__password = os.getenv("PASSWORD")

    def open_powershell(self) -> None:
        print("Opening PowerShell..")
        os.startfile("C:/Program Files/PowerShell/7/pwsh.exe")
        
    def functions(self) -> None:
        # Opens PowerShell if you press windows key and t 
        keyboard.add_hotkey("windows+t", self.open_powershell)
        keyboard.add_abbreviation("email",self.__email)
        keyboard.wait("ctrl+alt+t")


if __name__ == "__main__":
    App = ShortCutApp()
    App.functions()