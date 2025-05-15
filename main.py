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
        self.geometry("500x230")
        
        menu_bar = Menu(self)
        
        game_menu = Menu(menu_bar, tearoff=0)
        
        game_menu.add_command(label="Neues Spiel")
        game_menu.add_command(label="Beenden", command=self.quit)
        
        menu_bar.add_cascade(label="Spiel", menu=game_menu)
        
        self.config(menu=menu_bar)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.title_text = ctk.CTkLabel(self, text="Zahlenraten-Spiel", font=("Arial", 25))
        self.title_text.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="nsew")

        self.label_info = ctk.CTkLabel(self, text="Gib eine Zahl zwischen 0 und 100 ein!")
        self.label_info.grid(row=1, column=0, columnspan=2, pady=5)

        self.entry = ctk.CTkEntry(self, placeholder_text="Deine Zahl hier")
        self.entry.grid(row=2, column=0, columnspan=2, pady=5, padx=20, sticky="nsew")

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

        self.button = ctk.CTkButton(self, text="Raten")
        self.button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")


    def ask_player_new_game(self):
        self.msg = CTkMessagebox.CTkMessagebox(title="Info", message="Nochmal spielen?", corner_radius=3,
                                               option_1="Ja", option_2="Nein", icon="question")
        self.response = self.msg.get()

        if self.response == "Ja":
            self.reset_game()

        elif self.response == "Nein":
            self.quit()
        



if __name__ == "__main__":
    zahlenraten = ZahlenratenGUI()
    zahlenraten.mainloop()
    