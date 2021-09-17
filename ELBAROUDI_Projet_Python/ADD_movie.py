import os
from tkcalendar import *
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime
from PIL import ImageTk
import sys
from Evenement import Evenement
from Film import Film


film=Film()
py=sys.executable

root = Tk()
evenement = Evenement()
ev = Evenement()
class Add_movie:
    def __init__(self,root):
        self.root=root
        self.root.title("Ajouter un film")
        self.root.geometry("550x500")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/evenement.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()

        #Formulaire
            #Titre
        self.Titre = Label(self.root, text="Titre:", font=("Andalus", 15, 'bold'), bg='white',
                                   fg='black')
        self.Titre.place(x=250, y=10)

        self.Titre = Entry(self.root, font=("times new roman", 15))
        self.Titre.place(x=150, y=45, width=250)
        self.CheckTitre = Label(self.root, text='')

            # Genre
        self.Genre = Label(self.root, text="Genre:", font=("Andalus", 15, 'bold'), bg='white',
                           fg='black')
        self.Genre.place(x=250, y=80)

        self.Genre = Entry(self.root, font=("times new roman", 15))
        self.Genre.place(x=150, y=115, width=250)
        self.CheckGenre = Label(self.root, text='')

             # Dure
        self.Dure = Label(self.root, text="Dure:", font=("Andalus", 15, 'bold'), bg='white',fg='black')
        self.Dure.place(x=250, y=150)

        self.hour = Entry(self.root, font=("times new roman", 15))
        self.H = Entry(self.root, font=("times new roman", 15))
        self.hour.place(x=185, y=190, width=25)
        self.H.place(x=211, y=190, width=17)
        self.H.insert(0, "H")
        self.H.config(state="disabled")

        self.min = Entry(self.root, font=("times new roman", 15))
        self.m = Entry(self.root, font=("times new roman", 15))
        self.min.place(x=238, y=190, width=25)
        self.m.place(x=264, y=190, width=30)
        self.m.insert(0, "min")
        self.m.config(state="disabled")

        self.sec = Entry(self.root, font=("times new roman", 15))
        self.s = Entry(self.root, font=("times new roman", 15))
        self.sec.place(x=305, y=190, width=24)
        self.s.place(x=331, y=190, width=30)
        self.s.insert(0, "sec")
        self.s.config(state="disabled")
        self.CheckDure = Label(self.root, text='')

             # dateSortie
        self.dateSortie = Label(self.root, text="Date de sortie:", font=("Andalus", 15, 'bold'), bg='white',
                          fg='black')
        self.dateSortie.place(x=200, y=220)
        self.dateSortie = DateEntry(self.root, width=15, maxdate=datetime.now())

        self.dateSortie.place(x=150,y=255,width=250)
        self.CheckdateSortie = Label(self.root, text='')

            # Resume du film
        self.resumeFLM = Label(self.root, text="l'histoire du film:", font=("Andalus", 15, 'bold'), bg='white',
                                fg='black')
        self.resumeFLM.place(x=200, y=290)
        self.resume = Text(self.root, width=40, height=4)
        self.resume.insert(INSERT, "")
        self.resume.config(font=('Arial', 15))
        self.resume.place(x=50, y=325)
        self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.resume.yview)
        self.vsb.place(x=495, y=325, height=96)
        self.Checkresume = Label(self.root, text='')

        self.button = Button(self.root, text="Ajouter", activebackground="red",activeforeground="black", fg='white', bg="black", font=("Arial", 15, "bold"), command=lambda: self.add_data()).place(x=225  , y=450)

        # Fonction

    def add_data(self):

        if not self.Titre.get():
            self.CheckTitre.place(x=340, y=15)
            self.CheckTitre.config(text="*Vous avez laissé ce champ vide!!")
            return False
        else:
            self.CheckTitre.place(x=-100, y=-100)
            self.CheckTitre.config(text="")

        if not self.Genre.get():
            self.CheckGenre.place(x=340, y=85)
            self.CheckGenre.config(text="*Vous avez laissé ce champ vide!!")
            return False
        else:
            self.CheckGenre.place(x=-100, y=-100)
            self.CheckGenre.config(text="")

        if not self.hour.get() or not self.min.get() or not self.sec.get():
            self.CheckDure.place(x=340, y=155)
            self.CheckDure.config(text="*Vous avez laissé ce champ vide!!")
            return False
        else:
            testH = re.compile("[0-4]{1}")
            testM = re.compile("[0-5]|('') {1} [0-9]{1}")
            testS = re.compile("[0-5]|('') {1} [0-9]{1}")

            if testH.match(self.hour.get()) == None or testM.match(self.min.get()) == None or testS.match(
                self.sec.get()) == None:
                self.CheckDure.place(x=340, y=155)
                self.CheckDure.config(text="*Veuillez verifier la durée que vous avez tapé!!")
                return False
            else:

                self.CheckDure.place(x=-100, y=-100)
                self.CheckDure.config(text="")

        a = datetime.now().strftime("%Y-%m-%d")
        b = self.dateSortie.get_date()
        if str(b) == str(a):
            self.CheckdateSortie.place(x=340, y=225)
            self.CheckdateSortie.config(text="*Vous avez laissé ce champ vide!!")
            return False
        else:
            self.CheckdateSortie.place(x=-100, y=-100)
            self.CheckdateSortie.config(text="")

        if len(self.resume.get("1.0",END))<=1:
            self.Checkresume.place(x=365, y=295)
            self.Checkresume.config(text="*Vous avez laissé ce champ vide!!")
            return False
        else:
            self.Checkresume.place(x=-100, y=-100)
            self.Checkresume.config(text="")

        duree=str(self.hour.get())+":"+str(self.min.get())+":"+str(self.sec.get())
        film.setTitre(self.Titre.get().replace('\n', '').replace(' ', '&E&'))
        film.setGenre(self.Genre.get().replace('\n', '').replace(' ', '&E&'))
        film.setDure(duree.replace('\n', '').replace(' ', '&E&'))
        film.setDateSortie(str(self.dateSortie.get_date()))
        film.setResume(self.resume.get("1.0",END).replace('\n', '%L%').replace(' ', '&E&'))
        if film.findFlBy(None) == None:
            if film.addFilm() == True:
                messagebox.showinfo("Success", "Le film a été bien stocker!")
                root.destroy()
                os.system('%s %s' % (py, 'ADD_evenement.py'))
            else:
                messagebox.showerror("Error", "Something Goes Wrong")
        else:
            messagebox.showerror("WARNING", "Le nom du film que vous avez tapé est stocker dans le fichier !")


obj=Add_movie(root)
root.mainloop()