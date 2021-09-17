import os
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
from PIL import ImageTk
import sys
from Evenement import Evenement
from Film import Film
from Salle import Salle
py=sys.executable

root = Tk()
ev = Evenement()
evenement = Evenement()
flm = Film()
fl = Film()
salle= Salle()
sl=Salle()
FilmSelect = StringVar()
SalleSelect = StringVar()
class ADD_evenement:
        def __init__(self,root):
            self.root=root
            self.root.title("Ajouter un evenement")
            self.root.geometry("550x500")
            self.root.resizable(False,False)
            self.root.iconbitmap('images/libico.ico')

            #======== ADDING IMAGE ON ROOT WINDOW ========#
            self.image=ImageTk.PhotoImage(file="images/evenement.jpg")
            self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
            self.label.pack()
            #Fonction
            def add_movie():
                try:
                    root.destroy()
                    os.system('%s %s' % (py, 'ADD_movie.py'))
                except:
                    messagebox.showerror("Error", "Something Goes Wrong")

            def add_salle():
                try:
                    root.destroy()
                    os.system('%s %s' % (py, 'ADD_Salle.py'))
                except:
                    messagebox.showerror("Error", "Something Goes Wrong")

            #Formulaire
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
            listeOptions = ["Choisir un film"]
            for i in range(0, len(fl)):
                    listeOptions.append(fl[i].getTitre())

            FilmSelect.set(listeOptions[0])
            self.FilmTitre = OptionMenu(self.root, FilmSelect, *listeOptions)
            self.FilmTitre.place(x=150, y=60, width=250)
            self.CheckFilmSelect = Label(self.root, text='')


            self.Sallelabel = Label(self.root, text="Salle:", font=("Andalus", 15, 'bold'), bg='white', fg='black')
            self.Sallelabel.place(x=250, y=110)
            listeOptions = ["Choisir une salle"]
            for i in range(0, len(salle)):
                if salle[i].getDescription()=="Libre":
                    listeOptions.append(salle[i].getNumSalle())

            SalleSelect.set(listeOptions[0])
            self.salleNum = OptionMenu(self.root, SalleSelect, *listeOptions)
            self.salleNum.place(x=150, y=140, width=250)
            self.CheckSalleSelect = Label(self.root, text='')


            self.dateDiffusion = Label(self.root, text="Date de diffusion:", font=("Andalus", 15, 'bold'), bg='white',fg='black')
            self.dateDiffusion.place(x=200, y=190)
            self.CheckdateDiffusion = Label(self.root, text='')

            self.hour = Entry(self.root, font=("times new roman", 15))
            self.H = Entry(self.root, font=("times new roman", 15))
            self.hour.place(x=200, y=225, width=25)
            self.H.place(x=226, y=225, width=17)
            self.H.insert(0, "H")
            self.H.config(state="disabled")

            self.min = Entry(self.root, font=("times new roman", 15))
            self.m = Entry(self.root, font=("times new roman", 15))
            self.min.place(x=253, y=225, width=25)
            self.m.place(x=279, y=225, width=30)
            self.m.insert(0, "min")
            self.m.config(state="disabled")

            self.sec = Entry(self.root, font=("times new roman", 15))
            self.s = Entry(self.root, font=("times new roman", 15))
            self.sec.place(x=320, y=225, width=24)
            self.s.place(x=346, y=225, width=30)
            self.s.insert(0, "sec")
            self.s.config(state="disabled")

            self.JourDiffusion = DateEntry(self.root, width=15, mindate=datetime.now())

            self.JourDiffusion.place(x=150, y=260, width=250)


            self.button = Button(self.root, text="Ajouter", activebackground="red",
                                 activeforeground="black", fg='white', bg="black", font=("Arial", 15, "bold"),
                                 command=lambda: self.add_data()).place(x=240, y=300)

            self.button = Button(self.root, text="Ajouter un nouveau film", activebackground="red", activeforeground="black", fg='white',bg="black", font=("Arial", 15, "bold"), command=add_movie).place(x=150, y=390)
            self.button = Button(self.root, text="Ajouter une nouvelle salle", activebackground="red",activeforeground="black", fg='white', bg="black", font=("Arial", 15, "bold"),command=add_salle).place(x=150, y=450)
            # Fonction

        def add_data(self):

            if FilmSelect.get()=="Choisir un film":
                self.CheckFilmSelect.place(x=350, y=35)
                self.CheckFilmSelect.config(text="*Vous devez choisir un film!!")
                return False
            else:
                self.CheckFilmSelect.place(x=-100, y=-100)
                self.CheckFilmSelect.config(text="")

            if SalleSelect.get()=="Choisir une salle":
                self.CheckSalleSelect.place(x=350, y=115)
                self.CheckSalleSelect.config(text="*Vous devez choisir une salle!!")
                return False
            else:
                self.CheckSalleSelect.place(x=-100, y=-100)
                self.CheckSalleSelect.config(text="")

            if not self.hour.get() or not self.min.get() or not self.sec.get():
                self.CheckdateDiffusion.place(x=375, y=195)
                self.CheckdateDiffusion.config(text="*Vous avez laissé ce champ vide!!")
                return False
            else:
                verifyH = re.compile("[0-1]|('') {1} [0-9]{1}")
                verifyMS = re.compile("[0-5]|('') {1} [0-9]{1}")

                if verifyH.match(self.hour.get()) == None or verifyMS.match(self.min.get()) == None or verifyMS.match(self.sec.get()) == None:
                    self.CheckdateDiffusion.place(x=375, y=195)
                    self.CheckdateDiffusion.config(text="*The time format is incorrect!!")
                    return False
                else:

                    self.CheckdateDiffusion.place(x=-100, y=-100)
                    self.CheckdateDiffusion.config(text="")

            dateDiffusion = str(self.hour.get()) + ":" + str(self.min.get()) + ":" + str(self.sec.get())

            fl.setTitre(FilmSelect.get())
            flm= fl.findFlBy(None)

            sl.setNumSalle(SalleSelect.get())
            salle= sl.findSlBy(None)

            salle.setDescription("Occupe")

            evenement.setDateDiffusion(dateDiffusion)
            evenement.setJourDiffusion(str(self.JourDiffusion.get_date()))
            evenement.setNbPlaceReserver(0)

            # SALLE
            evenement.setIdSalle(salle.getIdSalle())
            evenement.setNumSalle(salle.getNumSalle())
            evenement.setDescription(salle.getDescription())
            evenement.setCapacite(salle.getCapacite())
            #Film
            evenement.setIdFilm(flm.getIdFilm())
            evenement.setTitre(flm.getTitre())
            evenement.setGenre(flm.getGenre())
            evenement.setDure(flm.getDure())
            evenement.setDateSortie(flm.getDateSortie())
            evenement.setResume(flm.getResume())
            #Tarif
            evenement.setIdTarif(int(1))
            evenement.setCout("58")
            evenement.setCategorie("adulte")

            if salle.updateSalle() == True:
                if evenement.addEvenement() == True:

                    messagebox.showinfo("Success", "L'evenement a été ajouter avec succes!")
                    root.destroy()
                else:
                    messagebox.showerror("Error", "Something Goes Wrong with file Evenements.txt")
            else:
                messagebox.showerror("WARNING", "Something Goes Wrong with file Salles.txt !")


obj=ADD_evenement(root)
root.mainloop()