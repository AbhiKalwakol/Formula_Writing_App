import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

def btn_type_enter():
    user_text = tk.Entry(app, font=("SF UI Display",13))
    user_text.grid(row=3, column=0)

    def btn_enter_enter():

        def btn_play_again():
            app.destroy()
            os.system('cmd /k "main.py"')

        if user_text.get() == compounds[compound]:
            final_label = tk.Label(app, text = "Correct", font=("SF UI Display",13),fg="#FAFAFA", bg="#0c1d37")
            final_label.grid(row= 4, column=0)
            play_again = tk.Button(app, text="Play Again",command = btn_play_again, font=("SF UI Display", 13),fg="#FAFAFA", bg="#207396")
            play_again.grid(row=5, column=0)

        else:
            final_label = tk.Label(app, text = "Wrong", font=("SF UI Display",13),fg="#FAFAFA", bg="#0c1d37")
            final_label.grid(row= 4, column=0)
            play_again = tk.Button(app, text="Play Again",command = btn_play_again, font=("SF UI Display", 13),fg="#FAFAFA", bg="#207396")
            play_again.grid(row=5, column=0)



    btn_enter = tk.Button(app, text="Enter",command = btn_enter_enter, font=("SF UI Display", 13),fg="#FAFAFA", bg="#207396")
    btn_enter.grid(row=3, column=1)


#Application
app = tk.Tk()
app.title("formula writing app")
app.geometry("550x400")
app.resizable(False, False)
app.configure(background="#FFF89A")
bg = PhotoImage(file="Images\\background.png")
bg_label = tk.Label(app, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Title
Title = tk.Label(app, text="Formula Writing Game", font=("SF UI Display", 30), fg="#FAFAFA", bg="#0c1d37").grid(row=0,column=0, columnspan=5, padx=10, pady=10)

#Random compound list
compounds = {
    "Pottasium Hydroxide": "KOH",
    "Sodium Hydroxide": "NaOH",
    "Aluminium Hydroxide": "Al(OH)3",
    "Zinc Hydroxide": "Zn(OH)2",
    "Ammonium Hydroxide": "NH3",
    "Cuprous Hydroxide": "Cu(OH)2",
    "Pottasium Sulphate": "K2SO4",
    "Sodium Sulphate": "Na2SO4",
    "Aluminium Sulphate": "Al2(SO4)3",
    "Zinc Sulphate": "ZnSO4",
    "Ammonium Sulphate": "(NH4)2SO4",
    "Cuprous Sulphate": "CuSO4",
    "Pottasium Nitrate": "KNO3",
    "Sodium Nitrate": "NaNO3",
    "Aluminium Nitrate": "Al(NO3)3",
    "Zinc Nitrate": "Zn(NO3)2",
    "Ammonium Nitrate": "NH4NO3",
    "Cuprous Nitrate": "Cu(NO3)2"
}

#Random compound
compounds_list = list(compounds.keys())

compound = random.choice(compounds_list)

compound_label = tk.Label(app, text=f"Compound : {compound} ",fg="#FAFAFA",bg="#0c1d37", font=("SF UI Display", 15) ).grid(row=1,column=0,columnspan=5, padx=10, pady=20)

#Type
btn_type = tk.Button(app, text="  Type  ", command=btn_type_enter, font=("SF UI Display", 13),fg="#FAFAFA", bg="#207396")

btn_type.grid(row=2,column=0, padx=10, pady=20)



app.mainloop()