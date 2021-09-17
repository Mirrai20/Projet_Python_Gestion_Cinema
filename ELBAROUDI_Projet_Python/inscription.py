from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import os
import sys

from Client import Client
from Employeur import Employeur
py=sys.executable
#pip install pillow

root = Tk()
descSelect = StringVar()
class Inscrire:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1014x595")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/login.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()


        #======== CREATING LABELS AND ENTRY BOX ON FRAME ========#
        self.Nomlabel=Label(self.root,text="Nom:",font=("Andalus",15,'bold'),bg='white',fg='black')
        self.Nomlabel.place(x=70,y=120)

        self.CheckNom = Label(self.root, text='')
        self.Nom=Entry(self.root,font=("times new roman",15))
        self.Nom.place(x=70,y=180,width=200)

        self.Prenomlabel=Label(self.root,text="Prenom:",font=("Andalus",15,'bold'),bg='white',fg='black')
        self.Prenomlabel.place(x=70,y=230)

        self.CheckPrenom = Label(self.root, text='')
        self.Prenom = Entry(self.root, font=("times new roman", 15))
        self.Prenom.place(x=70,y=280,width=200)
        ######
        self.userlabel = Label(self.root, text="Nom de compte:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.userlabel.place(x=370, y=120)

        self.CheckCompte = Label(self.root, text='')
        self.NomDeCompte = Entry(self.root, font=("times new roman", 15))
        self.NomDeCompte.place(x=370, y=180, width=250)

        self.passlabel = Label(self.root, text="Mot de passe:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.passlabel.place(x=370, y=230)

        self.Checkmdp = Label(self.root, text='')
        self.mdp = Entry(self.root, show="*", font=("times new roman", 15))
        self.mdp.place(x=370, y=280, width=250)
        ######
        self.userlabel = Label(self.root, text="Numéro de Téléphone:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.userlabel.place(x=700, y=120)

        self.ChecknumTele = Label(self.root, text='')
        self.numTele = Entry(self.root, font=("times new roman", 15))
        self.numTele.place(x=700, y=180, width=250)

        self.Desclabel = Label(self.root, text="Description:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.Desclabel.place(x=700, y=230)

        listeOptions = ('Client', 'Employeur')
        descSelect.set(listeOptions[0])
        self.description = OptionMenu(self.root, descSelect, *listeOptions)
        self.description.place(x=700, y=270, width=250)

        self.button=Button(self.root,text="Inscrire",activebackground="red",activeforeground="black",fg='white',bg="black",font=("Arial",15,"bold"),command=lambda :self.inscriredata())
        self.button.place(x=420,y=350,width=200)
        self.button = Button(self.root, text="Login", activebackground="red", activeforeground="black", fg='white',
                             bg="black", font=("Arial", 15, "bold"), command=lambda: self.login())
        self.button.place(x=420, y=400, width=200)
    def login(self):
        root.destroy()
        os.system('%s %s' % (py, 'Login.py'))

    def inscriredata(self):

       if not self.Nom.get():
            self.CheckNom.place(x=70,y=160)
            self.CheckNom.config(text="*Vous avez laissé ce champ vide!!")
            return False
       else:
           self.CheckNom.place(x=-100, y=-100)
           self.CheckNom.config(text="")

       if not self.Prenom.get():
            self.CheckPrenom.place(x=70,y=307)
            self.CheckPrenom.config(text="*Vous avez laissé ce champ vide!!")
            return False
       else:
           self.CheckPrenom.place(x=-100, y=-100)
           self.CheckPrenom.config(text="")

       if not self.NomDeCompte.get():
            self.CheckCompte.place(x=370, y=160)
            self.CheckCompte.config(text="*Vous avez laissé ce champ vide!!")
            return False
       else:
           self.CheckCompte.place(x=-100, y=-100)
           self.CheckCompte.config(text="")

       if not self.mdp.get():
            self.Checkmdp.place(x=370, y=307)
            self.Checkmdp.config(text="*Vous avez laissé ce champ vide!!")
            return False
       else:
           self.Checkmdp.place(x=-100, y=-100)
           self.Checkmdp.config(text="")


       if not self.numTele.get():
            self.ChecknumTele.place(x=700, y=160)
            self.ChecknumTele.config(text="*Vous avez laissé ce champ vide!!")
            return False
       else:
           if len(self.numTele.get()) != 10:
               self.ChecknumTele.place(x=700, y=160)
               self.ChecknumTele.config(text="*Ce numero de téléphone est invalide!!")
               return False
           Pattern = re.compile("(0){1}[6-7]{1}[0-9]{8}")

           if not Pattern.match(self.numTele.get()):
                       self.ChecknumTele.place(x=700, y=160)
                       self.ChecknumTele.config(text="*Ce numero de téléphone est invalide!!")
                       return False

           self.ChecknumTele.place(x=-100, y=-100)
           self.ChecknumTele.config(text="")

       if descSelect.get()=="Client":
           user=Client()
       elif descSelect.get()=="Employeur":
           user = Employeur()

        #on va retirer les espaces des chaines entrant pour faciliter le stockage ainsi que l'interprétation de donné from le fichier

       user.setNom(self.Nom.get().replace(' ', ''))
       user.setPrenom(self.Prenom.get().replace(' ', ''))
       user.setNomducompte(self.NomDeCompte.get().replace(' ', ''))
       user.setPassword(self.mdp.get().replace(' ', ''))
       user.setNumTele(self.numTele.get().replace(' ', ''))
       user.setVerified("PasVerifier")
       if user.findUsBy() == False:
           if user.addUser()==True:

              messagebox.showinfo("Success", "Félicitation, vous etes inscrit !")
              root.destroy()
              os.system('%s %s' % (py, 'Login.py'))
           else:
              messagebox.showerror("WARNING", "Erreur")
       else:
           utilisateur= user.findUsBy()
           if utilisateur.getNomducompte().upper() == self.NomDeCompte.get().replace(' ', '').upper():
              messagebox.showerror("WARNING", "Le nom du compte que vous avez tapé est déja utilisé !")
           if utilisateur.getNumTele() == self.numTele.get().replace(' ', ''):
               messagebox.showerror("WARNING", "Le numéro de téléphone que vous avez tapé est déja utilisé !")



obj=Inscrire(root)
root.mainloop()