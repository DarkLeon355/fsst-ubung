'''
Git-Uebungsaufgabe
Leon Maier & Julian Lengauer
FSST 4BHEL
2025
'''

import customtkinter as ctk
from tkinter import Menu
import CTkMessagebox


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class ZahlenratenGUI(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("Zahlenraten")
        self.geometry("500x500")
        
        menu_bar = Menu(self)
        
        game_menu = Menu(menu_bar, tearoff=0)
        
        game_menu.add_command(label="Neues Spiel")
        game_menu.add_command(label="Beenden", command=self.quit)
        
        menu_bar.add_cascade(label="Spiel", menu=game_menu)
        
        self.config(menu=menu_bar)
        
        self.title = ctk.CTkLabel(self, text="Zahlenraten", font=("Calibri", 20))
        self.title.grid(row=0, column=0, sticky="ew")
        



if __name__ == "__main__":
    zahlenraten = ZahlenratenGUI()
    zahlenraten.mainloop()
    