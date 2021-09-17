import os
from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk
import sys
from user import User
py=sys.executable

root = Tk()
user = User()
us = User()
class demande_inscription:
    def __init__(self,root):
        self.root=root
        self.root.title("Gestion de demandes d'inscription")
        self.root.geometry("800x500")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/alluser.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()
        #Fonctions
        def quitter():
             self.root.destroy()

        def accepter_demande():
            try:
                curItem = self.listTree.focus()
                idE = self.listTree.item(curItem)['text']
                if not idE:
                    messagebox.showerror("Error", "Veuillez choisir un evenement")
                    return False

                MsgBox = messagebox.askquestion('Exit Application',"Etes-vous sur de vouloir accepter cette demande ?",
                                                icon='warning')

                if MsgBox == 'yes':

                    us.setIdUser(idE)
                    if us.gerer_demande("Verifier") == True:
                        self.listTree.delete(curItem)
                        messagebox.showinfo('Return', "Cette demande d'inscription a été bien accepter")

                    else:
                        messagebox.showerror("WARNING", "Something Goes Wrong!")
                        return False

                else:
                    messagebox.showinfo('Return', "Aucune demande d'inscription n'a été accepter")

            except:
                messagebox.showerror("Error", "Something Goes Wrong!")

        def rejeter_demande():
            try:
                curItem = self.listTree.focus()
                idE = self.listTree.item(curItem)['text']
                if not idE:
                    messagebox.showerror("Error", "Veuillez choisir une demande")
                    return False

                MsgBox = messagebox.askquestion('Exit Application',
                                                "Etes-vous sur de vouloir rejeter cette demande ?",
                                                icon='warning')
                if MsgBox == 'yes':
                    us.setIdUser(idE)
                    if us.gerer_demande("Rejeter") == True:
                        self.listTree.delete(curItem)
                        messagebox.showinfo('Return', "Cette demande d'inscription a été bien rejeter")
                    else:
                        messagebox.showerror("WARNING", "Something Goes Wrong!")
                        return False

                else:
                    messagebox.showinfo('Return', "Aucune demande d'inscription n'a été rejeter")

            except:
                messagebox.showerror("Error", "Veuillez choisir une demande")

        def Affiche_design():
            try:
                # creating table

                self.listTree = ttk.Treeview(self.root, height=10, columns=(
                    'IDuser', 'Nom', 'Prenom', 'Numéro de Téléphone', 'Description', 'Nom de compte'))
                self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.listTree.yview)
                self.hsb = ttk.Scrollbar(self.root, orient="horizontal", command=self.listTree.xview)
                self.listTree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
                self.listTree.configure(yscrollcommand=self.vsb.set)
                self.listTree.heading("#0", text='IDuser', anchor='center')
                self.listTree.column("#0", width=111, anchor='center')
                self.listTree.heading("#1", text='Nom')
                self.listTree.column("#1", width=111, anchor='center')
                self.listTree.heading("#2", text='Prenom')
                self.listTree.column("#2", width=111, anchor='center')
                self.listTree.heading("#3", text='Numéro de Téléphone')
                self.listTree.column("#3", width=111, anchor='center')
                self.listTree.heading("#4", text='Description')
                self.listTree.column("#4", width=111, anchor='center')
                self.listTree.heading("#5", text='Nom de compte')
                self.listTree.column("#5", width=111, anchor='center')


                self.listTree.place(x=70, y=220, width=665)
                self.vsb.place(x=740, y=220, height=225)
                ttk.Style().configure("Treeview", font=('Times new Roman', 10))

                # label and input box
                self.label5 = Label(self.root, text="Les differentes fonctionnalités",bg="red",
                                    font=('Arial', 15, 'underline', 'bold'))
                self.label5.place(x=255, y=50)
                self.label6 = Label(self.root, text="Consulter les demandes d'inscription ", font=('Arial', 15, 'underline', 'bold'))
                self.label6.place(x=220, y=180)

                self.brt = Button(self.root, text="Quitter", width=15, font=('Algerian', 10), command=quitter).place(x=650,
                                                                                                                y=10)
                self.brt = Button(self.root, text="Rejeter la demande", bg="green", font=('Algerian', 10),
                                  command=rejeter_demande).place(x=180, y=100)
                self.brt = Button(self.root, text="Accepter la demande", bg="green", font=('Algerian', 10),command=accepter_demande).place(x=480, y=100)

            except:
                messagebox.showerror("Error", "Something Goes Wrong")
        def Afficher_data():
            try:

                if us.findAllUS() != None:
                    user = us.findAllUS()

                    for i in range(0, len(user)):
                        if user[i].getVerified().replace("\n","")=="PasVerifier":
                            self.listTree.insert("", 'end', text=user[i].getIdUser(), values=(
                            user[i].getNom(), user[i].getPrenom(), user[i].getNumTele(),
                            user[i].getDescription(), user[i].getNomducompte()))


                else:
                    messagebox.showerror("WARNING", "The user File is empty")

            except:
                messagebox.showerror("Error", "Something Goes Wrong")

        Affiche_design()
        Afficher_data()




obj=demande_inscription(root)
root.mainloop()