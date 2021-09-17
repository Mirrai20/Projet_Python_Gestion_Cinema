import os
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
import sys
from Evenement import Evenement
py=sys.executable

root = Tk()
evenement = Evenement()
ev = Evenement()
class reservation_managment:
    def __init__(self,root):
        self.root=root
        self.root.title("Gestion de reservations")
        self.root.geometry("800x500")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/alluser.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()


obj=reservation_managment(root)
root.mainloop()