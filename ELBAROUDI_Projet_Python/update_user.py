import os
from tkcalendar import *
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime
from PIL import ImageTk
import sys
from user import User
from Client import Client
from Employeur import Employeur
from Admin import Admin


#user=User()
py=sys.executable

root = Tk()
user=User()
user.setNomducompte(sys.argv[1])
us = user.findUsBy()

descSelect = StringVar()

class Upd_user:
    def __init__(self,root):
        self.root=root
        self.root.title("Modifier un utilisateur")
        self.root.geometry("550x650")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/add_user.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()

        #Formulaire

        self.Nomlabel = Label(self.root, text="Nom:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.Nomlabel.place(x=150, y=30)

        self.CheckNom = Label(self.root, text='',bg="red")
        self.Nom = Entry(self.root, font=("times new roman", 15))
        self.Nom.place(x=150, y=70, width=200)

        self.Nom.insert(0,us.getNom())

        self.Prenomlabel = Label(self.root, text="Prenom:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.Prenomlabel.place(x=150, y=115)

        self.CheckPrenom = Label(self.root, text='',bg="red")
        self.Prenom = Entry(self.root, font=("times new roman", 15))
        self.Prenom.place(x=150, y=155, width=200)

        self.Prenom.insert(0,us.getPrenom())
        ######
        self.userlabel = Label(self.root, text="Nom de compte:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.userlabel.place(x=150, y=200)

        self.CheckCompte = Label(self.root, text='',bg="red")
        self.NomDeCompte = Entry(self.root, font=("times new roman", 15))
        self.NomDeCompte.place(x=150, y=240, width=250)

        self.NomDeCompte.insert(0,us.getNomducompte())

        self.passlabel = Label(self.root, text="Mot de passe:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.passlabel.place(x=150, y=285)

        self.Checkmdp = Label(self.root, text='',bg="red")
        self.mdp = Entry(self.root, show="*", font=("times new roman", 15))
        self.mdp.place(x=150, y=325, width=250)

        self.mdp.insert(0,us.getPassword())

        ######
        self.userlabel = Label(self.root, text="Num??ro de T??l??phone:", font=("Andalus", 15, 'bold'), bg='white',
                               fg='black')
        self.userlabel.place(x=150, y=370)

        self.ChecknumTele = Label(self.root, text='',bg="red")
        self.numTele = Entry(self.root, font=("times new roman", 15))
        self.numTele.place(x=150, y=410, width=250)

        self.numTele.insert(0,us.getNumTele())

        self.Desclabel = Label(self.root, text="Description:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.Desclabel.place(x=150, y=455)

        listeOptions = ('Client', 'Employeur',"Admin")
        descSelect.set(us.getDescription())
        self.description = OptionMenu(self.root, descSelect, *listeOptions)
        self.description.place(x=150, y=505, width=250)



        self.button = Button(self.root, text="Modifier", activebackground="red",activeforeground="black", fg='white', bg="black", font=("Arial", 15, "bold"), command=lambda :self.stock_data()).place(x=220  , y=570)

        # Fonction
    def stock_data(self):
        if not self.Nom.get():
            self.CheckNom.place(x=350, y=35)
            self.CheckNom.config(text="*Vous avez laiss?? ce champ vide!!")
            return False
        else:
            self.CheckNom.place(x=-100, y=-100)
            self.CheckNom.config(text="")

        if not self.Prenom.get():
            self.CheckPrenom.place(x=350, y=120)
            self.CheckPrenom.config(text="*Vous avez laiss?? ce champ vide!!")
            return False
        else:
            self.CheckPrenom.place(x=-100, y=-100)
            self.CheckPrenom.config(text="")

        if not self.NomDeCompte.get():
            self.CheckCompte.place(x=350, y=205)
            self.CheckCompte.config(text="*Vous avez laiss?? ce champ vide!!")
            return False
        else:
            self.CheckCompte.place(x=-100, y=-100)
            self.CheckCompte.config(text="")

        if not self.mdp.get():
            self.Checkmdp.place(x=350, y=290)
            self.Checkmdp.config(text="*Vous avez laiss?? ce champ vide!!")
            return False
        else:
            self.Checkmdp.place(x=-100, y=-100)
            self.Checkmdp.config(text="")

        if not self.numTele.get():
            self.ChecknumTele.place(x=370, y=375)
            self.ChecknumTele.config(text="*Vous avez laiss?? ce champ vide!!")
            return False
        else:
            if len(self.numTele.get()) != 10:
                self.ChecknumTele.place(x=370, y=375)
                self.ChecknumTele.config(text="*veuillez verifier votre N??T??l??!!")
                return False
            Pattern = re.compile("(0){1}[6-7]{1}[0-9]{8}")

            if not Pattern.match(self.numTele.get()):
                self.ChecknumTele.place(x=370, y=375)
                self.ChecknumTele.config(text="*veuillez verifier votre N??T??l??!!")
                return False

            self.ChecknumTele.place(x=-100, y=-100)
            self.ChecknumTele.config(text="")

        if descSelect.get() == "Client":
            user = Client()
        elif descSelect.get() == "Employeur":
            user = Employeur()
        elif descSelect.get() == "Admin":
            user = Admin()

        # on va retirer les espaces des chaines entrant pour faciliter le stockage ainsi que l'interpr??tation de donn?? from le fichier
        user.setIdUser(us.getIdUser())
        user.setNom(self.Nom.get().replace(' ', ''))
        user.setPrenom(self.Prenom.get().replace(' ', ''))
        user.setNomducompte(self.NomDeCompte.get().replace(' ', ''))
        user.setPassword(self.mdp.get().replace(' ', ''))
        user.setNumTele(self.numTele.get().replace(' ', ''))
        user.setVerified("Verifier")
        if user.findUsBy() == False or (user.findUsBy().getNomducompte().upper()==us.getNomducompte().upper() and user.findUsBy().getNumTele()==us.getNumTele()):
           if user.updateUser() == True:

                messagebox.showinfo("Success", "Cet utilisateur a ??t?? bien modifier !")
                root.destroy()
           else:
                messagebox.showerror("WARNING", "Erreur")
        else:
           utilisateur = user.findUsBy()
           if utilisateur.getNomducompte().upper() == self.NomDeCompte.get().replace(' ', '').upper() and utilisateur.getNomducompte().upper()!=us.getNomducompte().upper():
             messagebox.showerror("WARNING", "Le nom du compte que vous avez tap?? est d??ja utilis?? !")
           if utilisateur.getNumTele() == self.numTele.get().replace(' ', '') and utilisateur.getNumTele()!=us.getNumTele() :
             messagebox.showerror("WARNING", "Le num??ro de t??l??phone que vous avez tap?? est d??ja utilis?? !")


obj=Upd_user(root)
root.mainloop()