import os
from tkcalendar import *
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime
from PIL import ImageTk
import sys
from Salle import Salle


salle=Salle()
py=sys.executable

root = Tk()
class Add_salle:
    def __init__(self,root):
        self.root=root
        self.root.title("Ajouter une salle")
        self.root.geometry("550x500")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/evenement.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()

        #Formulaire
            #NumSalle
        self.NumSalle = Label(self.root, text="Numéro du Salle:", font=("Andalus", 15, 'bold'), bg='white',
                                   fg='black')
        self.NumSalle.place(x=150, y=100)

        self.NumSalle = Entry(self.root, font=("times new roman", 15))
        self.NumSalle.place(x=150, y=140, width=250)
        self.CheckNumSalle = Label(self.root, text='',bg="red")

            # Capacite
        self.Capacite = Label(self.root, text="Capacité:", font=("Andalus", 15, 'bold'), bg='white',fg='black')
        self.Capacite.place(x=150, y=200)

        self.Capacite = Entry(self.root, font=("times new roman", 15))
        self.Capacite.place(x=150, y=240, width=250)
        self.CheckCapacite = Label(self.root, text='',bg="red")



        self.button = Button(self.root, text="Ajouter", activebackground="red",activeforeground="black", fg='white', bg="black", font=("Arial", 15, "bold"), command=lambda: self.add_data()).place(x=225  , y=300)

        # Fonction

    def add_data(self):
        try:
            numSl = int(self.NumSalle.get())
            self.CheckNumSalle.place(x=-100, y=-100)
            self.CheckNumSalle.config(text="")
        except ValueError:
            self.CheckNumSalle.place(x=150, y=168)
            self.CheckNumSalle.config(text="*Veulliez verifier ce que vous avez saisi!!")
            return False

        try:
            capSl = int(self.Capacite.get())
            self.CheckCapacite.place(x=-100, y=-100)
            self.CheckCapacite.config(text="")
        except ValueError:
            self.CheckCapacite.place(x=150, y=268)
            self.CheckCapacite.config(text="*Veulliez verifier ce que vous avez saisi!!")
            return False

        salle.setNumSalle(str(numSl))
        salle.setCapacite(capSl)
        salle.setDescription("Libre")
        if salle.findSlBy(None) == None:
            if salle.addSalle() == True:

                messagebox.showinfo("Success", "La salle a été bien stocker!")
                root.destroy()
                os.system('%s %s' % (py, 'ADD_evenement.py'))
            else:
                messagebox.showerror("Error", "Something Goes Wrong")
        else:
            messagebox.showerror("WARNING", "Le numéro de salle que vous avez tapé est déja stocké dans le fichier !")





obj=Add_salle(root)
root.mainloop()