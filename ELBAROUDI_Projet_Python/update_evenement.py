import os
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
import sys

from tkcalendar import DateEntry
from datetime import datetime, date

from Evenement import Evenement
from Film import Film
from Salle import Salle
py=sys.executable

root = Tk()
evenement = Evenement()
ev = Evenement()
flm = Film()
fl = Film()
salle= Salle()
sl=Salle()
FilmSelect = StringVar()
SalleSelect = StringVar()
class Update_Evenement:
    def __init__(self,root):
        self.root=root
        self.root.title("Modifier un evenement")
        self.root.geometry("550x400")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/evenement.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()

        # Formulaire
        if evenement.findEvBy(sys.argv[1], 'Evenements.txt') != None:
            ev = evenement.findEvBy(sys.argv[1], 'Evenements.txt')
        else:
            return False
        if flm.findAllFl() != None:
            fl = flm.findAllFl()
        else:
            return False
        if sl.findAllSl() != None:
            salle = sl.findAllSl()
        else:
            return False

        self.Filmlabel = Label(self.root, text="Film:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.Filmlabel.place(x=250, y=30)
        listeOptions = [ev.getTitre()]
        for i in range(0, len(fl)):
          if fl[i].getTitre()!= ev.getTitre():
             listeOptions.append(fl[i].getTitre())

        FilmSelect.set(listeOptions[0])

        self.description = OptionMenu(self.root, FilmSelect, *listeOptions)

        self.description.place(x=150, y=65, width=250)

        self.Sallelabel = Label(self.root, text="Salle:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
        self.Sallelabel.place(x=250, y=115)
        # if salle est libre, on va afficher que les salles qui ont libre
        listeOptions = [ev.getNumSalle()]
        for i in range(0, len(salle)):
            if salle[i].getNumSalle() != ev.getNumSalle() and salle[i].getDescription()=="Libre":
                listeOptions.append(salle[i].getNumSalle())

        SalleSelect.set(listeOptions[0])
        self.description = OptionMenu(self.root, SalleSelect, *listeOptions)
        self.description.place(x=150, y=150, width=250)

        self.dateDiffusion = Label(self.root, text="Date de diffusion:", font=("Andalus", 15, 'bold'), bg='white',
                                   fg='black')
        self.dateDiffusion.place(x=200, y=190)

        partie = ev.getDateDiffusion().split(':')
        self.hour = Entry(self.root, font=("times new roman", 15))
        self.H = Entry(self.root, font=("times new roman", 15))
        self.hour.place(x=200, y=225, width=25)
        self.H.place(x=226, y=225, width=17)
        self.hour.insert(0, partie[0])
        self.H.insert(0,"H")
        self.H.config(state="disabled")

        self.min = Entry(self.root, font=("times new roman", 15))
        self.m = Entry(self.root, font=("times new roman", 15))
        self.min.place(x=253, y=225, width=25)
        self.m.place(x=279, y=225, width=30)
        self.min.insert(0, partie[1])
        self.m.insert(0, "min")
        self.m.config(state="disabled")

        self.sec = Entry(self.root, font=("times new roman", 15))
        self.s = Entry(self.root, font=("times new roman", 15))
        self.sec.place(x=320, y=225, width=24)
        self.s.place(x=346, y=225, width=30)
        self.sec.insert(0, partie[2])
        self.s.insert(0,"sec")
        self.s.config(state="disabled")


        self.JourDiffusion = DateEntry(self.root, width=15, mindate=datetime.now())

        self.JourDiffusion.place(x=150, y=260, width=250)
        date1 = datetime.strptime(ev.getJourDiffusion(), "%Y-%m-%d")
        self.JourDiffusion.set_date(date1)
        self.CheckdateDiffusion = Label(self.root, text='')

        self.button = Button(self.root, text="Modifier", activebackground="red",
                             activeforeground="black", fg='white', bg="black", font=("Arial", 15, "bold"),
                             command=lambda: self.add_data()).place(x=240, y=310)

    def add_data(self):
        if not self.hour.get() or not self.min.get() or not self.sec.get():
            self.CheckdateDiffusion.place(x=375, y=195)
            self.CheckdateDiffusion.config(text="*Vous avez laissé ce champ vide!!")
            return False
        else:
            verifyH = re.compile("[0-1]|('') {1} [0-9]{1}")
            verifyMS = re.compile("[0-5]|('') {1} [0-9]{1}")

            if verifyH.match(self.hour.get()) == None or verifyMS.match(self.min.get()) == None or verifyMS.match(
                    self.sec.get()) == None:
                self.CheckdateDiffusion.place(x=375, y=195)
                self.CheckdateDiffusion.config(text="*The time format is incorrect!!")
                return False
            else:

                self.CheckdateDiffusion.place(x=-100, y=-100)
                self.CheckdateDiffusion.config(text="")

        if evenement.findEvBy(sys.argv[1], 'Evenements.txt') != None:
            ev = evenement.findEvBy(sys.argv[1], 'Evenements.txt')
        else:
            return False
        fl.setTitre(FilmSelect.get())
        flm = fl.findFlBy(None)

        sl.setNumSalle(SalleSelect.get())
        salle = sl.findSlBy(None)

        dateDiffusion = str(self.hour.get()) + ":" + str(self.min.get()) + ":" + str(self.sec.get())

        if ev.getNumSalle()!=SalleSelect.get():
            ev.setIdSalle(salle.getIdSalle())
            #Changer la description de la nouvelle salle vers "Occuper"
            salle.setDescription("Occupe")
            if salle.updateSalle() != True:
                messagebox.showerror("WARNING", "Something Goes Wrong with file Salles.txt !")
            sl.setNumSalle(ev.getNumSalle())

            ev.setIdSalle(salle.getIdSalle())
            salle = sl.findSlBy(None)
            salle.setDescription("Libre")
            #Changer la description de l'ancienne salle vers "Libre"
            if salle.updateSalle() != True:
                messagebox.showerror("WARNING", "Something Goes Wrong with file Salles.txt !")

        ev.setIdFilm(flm.getIdFilm())
        ev.setDateDiffusion(dateDiffusion)
        ev.setJourDiffusion(str(self.JourDiffusion.get_date()))

        if ev.updateEvenement() == True:

            messagebox.showinfo("Success", "Cet evenement a été modifier avec succes!")
            root.destroy()
        else:
            messagebox.showerror("Error", "Something Goes Wrong with file Evenements.txt")


obj=Update_Evenement(root)
root.mainloop()