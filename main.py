import tkinter
import tkinter as tk
from  tkinter import *
import customtkinter as customtkinter
from  customtkinter import *
import Navbar
from Entities.Coffee import *
import DataAccess.CoffeeDal as c
from DataAccess.CoffeeDal import *
import Navbar as n
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("700x500")
app.configure(bg="#F0F2B6")

def ExitWin():
    app.destroy()

def addData():
    pass

def AddCoffee():
    f = Frame(bg="#F0F2B6", height=1000, width=1000)
    f.place(x=0, y=0)
    mystring = tk.StringVar(app)
    name = customtkinter.CTkEntry(master=app, textvariable=mystring, placeholder_text="Ürün adı")
    name.pack()
    mystring1 = tk.StringVar(app)

    def getvalue1():
        name = mystring.get()
        price = (mystring1.get())
        c.CoffeeDal.Add(name,price)
        Label = tk.Label(text="Yeni Ürün Ekledi", bg="#F0F2B6", fg="#224B0C", font="Verdana 25")
        Label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    price = customtkinter.CTkEntry(master=app, textvariable=mystring1, placeholder_text="Ürün adı")
    price.pack()
    button2 = tk.Button(app,
                        text='Submit',
                        fg='White',
                        bg='dark green', height=1, width=10, command=getvalue1)
    button2.pack()
    exit()

def exit():
 button = customtkinter.CTkButton(master=app,text="Çıkış",
                                         fg_color="#4C0033", text_font="Verdana 18", text_color="#F0F2B6",
                                         command=ExitWin)
 button.place(x=30,y=10)
def addCoffee():
    button = customtkinter.CTkButton(master=app, text="Ürün Ekle",
                                     fg_color="#3D8361", text_font="Verdana 18", text_color="#F0F2B6",
                                     command=AddCoffee)
    button.place(x=180,y=10)
def DeleteProduct(self):
    c.CoffeeDal.Delete(self)
def deleteProduct():
    button = customtkinter.CTkButton(master=app, text="Ürün Sil",
                                     fg_color="#E94560", text_font="Verdana 18", text_color="#F0F2B6",
                                     command=DeleteProduct)
    button.place(x=330, y=10)
def start():
    f = Frame(bg="#F0F2B6",height=1000,width=1000)
    f.place(x=0,y=0)
    f = customtkinter.CTkFrame(master=app, width=20000,
                               height=20000,
                               corner_radius=10, bg_color="#F0F2B6", border_color="#F0F2B6", fg_color="#F0F2B6")
    f.place(x=0, y=40)
    n.getalllist(f)

    exit()
    addCoffee()
    deleteProduct()







    c.CoffeeDal.GetAllForPrice("Coffees")
Label = tk.Label(text="Günaydın", bg="#F0F2B6",fg="#224B0C",font="Verdana 25")
button = customtkinter.CTkButton(master=app, text="Başlat",fg_color="#224B0C",text_font="Verdana 18",text_color="#F0F2B6",command=start)
Label.place(x=270,y=150)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
exit()
addCoffee()

app.mainloop()