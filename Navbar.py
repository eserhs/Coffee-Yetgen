import time

import customtkinter
import tkinter as tk
from  tkinter import *
import DataAccess.CoffeeDal as c

def getal(app):
    Label = tk.Label(text="kahve çeşitleri", bg="#F0F2B6", fg="#224B0C", font="Verdana 25")
    Label.place(x=7, y=50)
    listbox = Listbox(master=app, font="Verdana 18", bg="#F0F2B6", fg="#224B0C", relief="flat",
                      bd="1 px", height=700, width=30, selectbackground="#224B0C", activestyle="none",
                      highlightthickness="0 px"
                      , selectforeground="#F0F2B6")
    listbox.place(x=8, y=55)
    scrollbar = Scrollbar()
    scrollbar.pack(side=RIGHT, fill=BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    c.CoffeeDal.GetAllForName("Coffees", listbox)
    scrollbar.config(command=listbox.yview)
    def CurSelet(e):
        f = Frame(bg="#F0F2B6", height=1000, width=1000)
        f.place(x=0, y=0)
        Label = tk.Label(text="Kahveniz Hazırlanıyor... ", bg="#F0F2B6", fg="#224B0C", font="Verdana 25")
        Label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    listbox.bind('<<ListboxSelect>>', CurSelet)


def getalllist(app):
    button = customtkinter.CTkButton(master=app, text="Ürün Ekle", width=80,
                                     height=32,
                                     fg_color="#3D8361", text_font="Verdana 12", text_color="#F0F2B6",
                                     bg_color="#E0D98C", corner_radius=10, command=getal(app))