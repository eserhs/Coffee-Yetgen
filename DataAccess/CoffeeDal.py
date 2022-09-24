import Entities.Coffee
import sqlite3
import tkinter  as tk
from  tkinter import *

from  customtkinter import *

class CoffeeDal(Entities.Coffee.Coffee):
  def __init__(self,name,price):
    super(CoffeeDal, self).__init__(name, price)



  def Add(name,price):
    connect = sqlite3.connect("Coffee.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Coffees(name TEXT,price INT)")
    Add_Command = "INSERT INTO Coffees VALUES{}"
    data = (name,price)
    cursor.execute(Add_Command.format(data))
    connect.commit()
    connect.close()


  def Delete(self):
    connect = sqlite3.connect("Coffee.db")
    cursor = connect.cursor()
    Delete_command = "DELETE FROM Coffees WHERE name = '{}'"
    data = (self.name)
    cursor.execute(Delete_command.format(data))
    connect.commit()
    connect.close()

  def Update(self, UpdateData):
    connect = sqlite3.connect("Coffee.db")
    cursor = connect.cursor()
    Update_command = "UPDATE Coffees SET price = {} WHERE price = '{}' "
    data = (self.price)
    cursor.execute(Update_command.format(UpdateData,data))
    connect.commit()
    connect.close()


  def GetAllForName(self,liste):
    connect = sqlite3.connect("Coffee.db")
    cursor = connect.cursor()
    GetAll_command = "SELECT name FROM {}"
    data = self
    cursor.execute(GetAll_command.format(data))
    list_all = cursor.fetchall()


    for i in list_all:
        liste.insert(END,i)
    connect.commit()
    connect.close()


  def GetAllForPrice(self):
      connect = sqlite3.connect("Coffee.db")
      cursor = connect.cursor()
      GetAll_command = "SELECT price FROM '{}'"
      data = self
      cursor.execute(GetAll_command.format(data))
      list_all = cursor.fetchall()
      Label = tk.Label(text="Fiyat", bg="#F0F2B6", fg="#224B0C", font="Verdana 25")
      Label.place(x=490, y=50)
      liste = Listbox(font="Verdana 18", bg="#F0F2B6", fg="#224B0C", relief="flat",
                      bd="1 px", height=700, width=30, selectbackground="#F0F2B6", activestyle="none",
                      highlightthickness="0 px",selectforeground="#CA955C")


      for i in list_all:
        j = "{} ₺".format(i)
        liste.insert(END,j)
      liste.place(x=500, y=90)
      connect.commit()
      connect.close()










