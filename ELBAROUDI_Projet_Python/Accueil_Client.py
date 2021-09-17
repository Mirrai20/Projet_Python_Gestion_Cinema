from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import os
import sys
from Evenement import  Evenement
from datetime import datetime, timedelta

py=sys.executable
root=Tk()
evenement = Evenement()
ev = Evenement
#creating window
class Accueil_Client(Tk):
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap('images/libico.ico')
        self.root.title("Accueil Client")
        self.root.geometry("1320x768")
        self.root.resizable(False,False)

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/sset2.png")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()

        # ======== Fonctions ========#

        def affiche_detail():
            try:
                curItem = self.listTree.focus()
                idEv = int(self.listTree.item(curItem)['text'])
                os.system('%s %s' % (py, 'detail_Film.py' + ' ' + str(idEv)))
            except:
                messagebox.showerror("Error", "Veuillez choisir un evenement")

        def log():
            self.root.destroy()
            os.system('%s %s' % (py, 'Login.py'))
            exit()

        def Reserver():
            try:
                curItem = self.listTree.focus()
                idEv = int(self.listTree.item(curItem)['text'])
                MsgBox = messagebox.askquestion('Exit Application', 'Etes-vous sur de reserver un billet pour cet evenement ?',
                                                   icon='warning')
                if MsgBox == 'yes':
                    ev = evenement.findEvBy(str(idEv), 'Evenements.txt')
                    print(ev.getNbPlaceReserver())
                    ev.setNbPlaceReserver(int(ev.getNbPlaceReserver())+1)
                    print(ev.getNbPlaceReserver())
                    if ev.updateEvenement() == True:
                        messagebox.showinfo('Return', 'Félicitation vous avez réservé votre billet avec succès!!')
                        tous_evenement()
                    else:
                        messagebox.showerror("Error", "Something Goes Wrong with file Evenements.txt")

                else:
                    messagebox.showinfo('Return', "Veuillez choisir un autre evenement")


            except:
                messagebox.showerror("Error", "Veuillez choisir un evenement")

        def Trois_jour():
            for record in self.listTree.get_children():
                self.listTree.delete(record)

            now = datetime.now()
            dt = now + timedelta(days=+3)
            ev = evenement.findAllEv()
            for i in range(0, len(ev)):
                if datetime.strptime(ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(),
                                     '%Y-%m-%d %H:%M:%S') <= dt:
                    self.listTree.insert("", 'end', text=ev[i].getIDevenement(), values=(
                        ev[i].getTitre(), ev[i].getNumSalle(), ev[i].getCapacite(),
                        ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(), ev[i].getNbPlaceReserver(),
                        ev[i].getCout().replace('\n', '') + ' €'))

        def semain_encours():
            for record in self.listTree.get_children():
                self.listTree.delete(record)

            now = datetime.now()
            dt = now + timedelta(weeks=+1)
            ev = evenement.findAllEv()
            for i in range(0, len(ev)):
                if datetime.strptime(ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(),
                                     '%Y-%m-%d %H:%M:%S') <= dt:
                    self.listTree.insert("", 'end', text=ev[i].getIDevenement(), values=(
                        ev[i].getTitre(), ev[i].getNumSalle(), ev[i].getCapacite(),
                        ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(), ev[i].getNbPlaceReserver(),
                        ev[i].getCout().replace('\n', '') + ' €'))

        def semain_avenir():
            for record in self.listTree.get_children():
                self.listTree.delete(record)

            now = datetime.now()
            ev = evenement.findAllEv()
            dt1 = now + timedelta(weeks=+1)
            dt2 = now + timedelta(weeks=+2)

            for i in range(0, len(ev)):
                Mdt = datetime.strptime(ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(), '%Y-%m-%d %H:%M:%S')
                if Mdt <= dt2 and Mdt >= dt1:
                    self.listTree.insert("", 'end', text=ev[i].getIDevenement(), values=(
                        ev[i].getTitre(), ev[i].getNumSalle(), ev[i].getCapacite(),
                        ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(), ev[i].getNbPlaceReserver(),
                        ev[i].getCout().replace('\n', '') + ' €'))

        def mois_avenir():
            for record in self.listTree.get_children():
                self.listTree.delete(record)

            now = datetime.now()
            dt = now + timedelta(days=+30)
            ev = evenement.findAllEv()
            for i in range(0, len(ev)):
                if datetime.strptime(ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(),
                                     '%Y-%m-%d %H:%M:%S') <= dt:
                    self.listTree.insert("", 'end', text=ev[i].getIDevenement(), values=(
                        ev[i].getTitre(), ev[i].getNumSalle(), ev[i].getCapacite(),
                        ev[i].getJourDiffusion() + ' ' + ev[i].getDateDiffusion(), ev[i].getNbPlaceReserver(),
                        ev[i].getCout().replace('\n', '') + ' €'))

        def tous_evenement():
            for record in self.listTree.get_children():
                self.listTree.delete(record)
            Afficher_data()

        def Affiche_design():
            try:
                # creating table

                self.listTree = ttk.Treeview(self.root, height=14, columns=(
                'IDEvenement', 'Titre du film', 'Numéro du salle', 'Capactié', 'Date de diffusion', 'Place reservé',
                'Tarif'))
                self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.listTree.yview)
                self.hsb = ttk.Scrollbar(self.root, orient="horizontal", command=self.listTree.xview)
                self.listTree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
                self.listTree.configure(yscrollcommand=self.vsb.set)
                self.listTree.heading("#0", text='IDEvenement', anchor='center')
                self.listTree.column("#0", width=111, anchor='center')
                self.listTree.heading("#1", text='Titre du film')
                self.listTree.column("#1", width=111, anchor='center')
                self.listTree.heading("#2", text='Numéro du salle')
                self.listTree.column("#2", width=111, anchor='center')
                self.listTree.heading("#3", text='Capactié')
                self.listTree.column("#3", width=111, anchor='center')
                self.listTree.heading("#4", text='Date de diffusion')
                self.listTree.column("#4", width=111, anchor='center')
                self.listTree.heading("#5", text='Place reservé')
                self.listTree.column("#5", width=111, anchor='center')
                self.listTree.heading("#6", text='Tarif')
                self.listTree.column("#6", width=111, anchor='center')

                self.listTree.place(x=270, y=360, width=778)
                self.vsb.place(x=1050, y=360, height=307)
                # self.hsb.place(x=160, y=650, width=1000)
                ttk.Style().configure("Treeview", font=('Times new Roman', 10))

                # label and input box
                self.label3 = Label(self.root, text='Client: Page accueil', fg='black', bg="white", font=('AlGERIAN', 30, 'bold'))
                self.label3.place(x=50, y=22)

                self.label6 = Label(self.root, text="Consulter tous les événements", bg='red',font=('Arial', 15, 'underline', 'bold'))
                self.label6.place(x=540, y=200)
                self.button = Button(self.root, text='Tous les événements', font=('Arial', 10, 'bold'), command=tous_evenement).place(x=190, y=300)
                self.button = Button(self.root, text='La semaine en cours', font=('Arial', 10, 'bold'), command=semain_encours).place(x=410, y=300)
                self.brt = Button(self.root, text="Les trois derniers jours", font=('Arial', 10, 'bold'), command=Trois_jour).place(x=620,y=300)
                self.brt = Button(self.root, text="La semaine à venir", font=('Arial', 10, 'bold'), command=semain_avenir).place(x=830,y=300)
                self.brt = Button(self.root, text="Le mois à venir", font=('Arial', 10, 'bold'), command=mois_avenir).place(x=1040,y=300)
                self.brt = Button(self.root, text="LOGOUT", width=15, font=('Algerian', 10), command=log).place(x=1180,y=10)
                self.brt = Button(self.root, text="réserver", bg="green", width=15, font=('Algerian', 10),command=Reserver).place(x=935, y=250)
                self.brt = Button(self.root, text="Détail sur le film", bg="green", width=15, font=('Algerian', 10),command=affiche_detail).place(x=310, y=250)

            except:
                messagebox.showerror("Error", "Something Goes Wrong")

        def Afficher_data():
            try:

                if evenement.findAllEv()!=None:
                    ev = evenement.findAllEv()

                    for i in range(0,len(ev)):
                        self.listTree.insert("", 'end', text=ev[i].getIDevenement(),values=(ev[i].getTitre(), ev[i].getNumSalle(), ev[i].getCapacite(), ev[i].getJourDiffusion()+' '+ev[i].getDateDiffusion(), ev[i].getNbPlaceReserver(),ev[i].getCout().replace('\n', '')+' €'))


                else:
                    messagebox.showerror("WARNING","File empty")

            except:
                messagebox.showerror("Error", "Something Goes Wrong")



        Affiche_design()
        Afficher_data()











obj=Accueil_Client(root)
root.mainloop()
