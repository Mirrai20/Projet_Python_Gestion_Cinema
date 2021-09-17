from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import os
import sys
from user import User


user = User()
py=sys.executable
#pip install pillow

root = Tk()
class Login:
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
        self.userlabel=Label(self.root,text="Nom de compte:",font=("Andalus",15,'bold'),bg='white',fg='black')
        self.userlabel.place(x=400,y=120)

        self.NomDeCompte=Entry(self.root,font=("times new roman",15))
        self.NomDeCompte.place(x=400,y=170,width=250)
        self.CheckCompte= Label(self.root, text='')


        self.passlabel=Label(self.root,text="Mot de passe:",font=("Andalus",15,'bold'),bg='white',fg='black')
        self.passlabel.place(x=400,y=220)

        self.Checkmdp = Label(self.root, text='')
        self.mdp = Entry(self.root, show="*", font=("times new roman", 15))
        self.mdp.place(x=400,y=270,width=250)


        self.button=Button(self.root,text="LOGIN",activebackground="red",activeforeground="black",fg='white',bg="black",font=("Arial",15,"bold"),command=lambda :self.logindata())
        self.button.place(x=420,y=320,width=200)

        self.button = Button(self.root, text="S'authentifier", activebackground="red", activeforeground="black", fg='white',bg="black", font=("Arial", 15, "bold"), command=lambda: self.inscription())
        self.button.place(x=420, y=370, width=200)

    def inscription(self):
        root.destroy()
        os.system('%s %s' % (py, 'inscription.py'))

    def logindata(self):
        if not self.NomDeCompte.get():
            self.CheckCompte.place(x=680, y=172)
            self.CheckCompte.config(text="*Vous avez laissé ce champ vide!!")
            return False
        if not self.mdp.get():
            self.Checkmdp.place(x=680, y=272)
            self.Checkmdp.config(text="*Vous avez laissé ce champ vide!!")
            return False
        user.setNomducompte(self.NomDeCompte.get())
        user.setPassword(self.mdp.get())
        if user.findUsBy() != False:
            utilisateur= user.findUsBy()
            if utilisateur.getPassword() == self.mdp.get():

                if utilisateur.getVerified().replace('\n', '') != "PasVerifier":
                    messagebox.showinfo("Success", "Hello !"+utilisateur.getDescription())
                    root.destroy()
                    os.system('%s %s' % (py, 'Accueil_'+utilisateur.getDescription()+'.py'))
                else:
                    messagebox.showinfo("WARNING", "Hello !" + utilisateur.getDescription() + " : Ton compte n'est pas encore vérifié \n veuillez patienter un peu.")
            else:
                messagebox.showerror("WARNING", "Nom du compte ou mot de passe incorrect")
        else:
            messagebox.showerror("WARNING","Nom du compte ou mot de passe incorrect")



obj=Login(root)
root.mainloop()