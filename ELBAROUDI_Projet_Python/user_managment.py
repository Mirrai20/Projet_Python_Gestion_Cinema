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
class User_mng:
    def __init__(self,root):
        self.root=root
        self.root.title("Gestion des utilisateurs")
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

        def del_user():
            try:
                curItem = self.listTree.focus()
                idE = self.listTree.item(curItem)['text']

                if not idE:
                    messagebox.showerror("Error", "Veuillez choisir un utilisateur")
                    return False

                MsgBox = messagebox.askquestion('Exit Application',
                                                "Etes-vous sur de vouloir supprimer cet utilisateur ?",
                                                icon='warning')
                if MsgBox == 'yes':
                    us.setIdUser(idE)
                    if us.deleteUser() == True:
                        self.listTree.delete(curItem)
                        messagebox.showinfo('Return', "Cet utilisateur a été bien supprimer")
                    else:
                        messagebox.showerror("WARNING", "Something Goes Wrong!")
                        return False

                else:
                    messagebox.showinfo('Return', "Aucune utilisateur n'a été supprimer")

            except:
                messagebox.showerror("Error", "Veuillez choisir un utilisateur")

        def Add_user():
            try:
                os.system('%s %s' % (py, 'ADD_user.py'))
                for record in self.listTree.get_children():
                    self.listTree.delete(record)
                Afficher_data()
            except:
                messagebox.showerror("Error", "Something Goes Wrong")

        def Upd_user():
            try:
                curItem = self.listTree.focus()
                Ncmp = str(self.listTree.item(curItem)['values'][4])
                os.system('%s %s' % (py, 'update_user.py' + ' ' + Ncmp))
                for record in self.listTree.get_children():
                    self.listTree.delete(record)
                Afficher_data()
            except:
                messagebox.showerror("Error", "Veuillez choisir un utilisateur")

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
                self.brt = Button(self.root, text="Ajouter un utilisateur", bg="green", font=('Algerian', 10),
                                  command=Add_user).place(x=120, y=100)
                self.brt = Button(self.root, text="Modifier un utilisateur", bg="green", font=('Algerian', 10),command=Upd_user).place(x=320, y=100)
                self.brt = Button(self.root, text="Supprimer un utilisateur", bg="green", font=('Algerian', 10),command=del_user).place(x=520, y=100)

            except:
                messagebox.showerror("Error", "Something Goes Wrong")
        def Afficher_data():
            try:

                if us.findAllUS() != None:
                    user = us.findAllUS()

                    for i in range(0, len(user)):
                        self.listTree.insert("", 'end', text=user[i].getIdUser(), values=(
                        user[i].getNom(), user[i].getPrenom(), user[i].getNumTele(),
                        user[i].getDescription(), user[i].getNomducompte()))


                else:
                    messagebox.showerror("WARNING", "The user File is empty")

            except:
                messagebox.showerror("Error", "Something Goes Wrong")

        Affiche_design()
        Afficher_data()




obj=User_mng(root)
root.mainloop()