from tkinter import *
from tkinter import ttk

from PIL import ImageTk
import sys
from Evenement import Evenement
py=sys.executable

root = Tk()
evenement = Evenement()
ev = Evenement()
class Detail_Film:
    def __init__(self,root):
        self.root=root
        self.root.title("Detail sur le film")
        self.root.geometry("550x400")
        self.root.resizable(False,False)
        self.root.iconbitmap('images/libico.ico')

        #======== ADDING IMAGE ON ROOT WINDOW ========#
        self.image=ImageTk.PhotoImage(file="images/detail_film.jpg")
        self.label=Label(self.root,image=self.image)#ADDED IMAGE ON LABEL
        self.label.pack()

        if evenement.findEvBy(sys.argv[1], 'Evenements.txt') != None:
            ev = evenement.findEvBy(sys.argv[1], 'Evenements.txt')
        else:
            return False
        #======== CREATING LABELS AND ENTRY BOX ON FRAME ========#
        self.label6 = Label(self.root, text="Titre: "+ ev.getTitre(),
                        font=('Arial', 15, 'underline', 'bold'))
        self.label6.place(x=50, y=50 , width=450)

        self.label6 = Label(self.root, text="Genre: "+ev.getGenre(),
                            font=('Arial', 15, 'underline', 'bold'))
        self.label6.place(x=50, y=90 , width=450)

        self.label6 = Label(self.root, text="Dure: "+ ev.getDure(),
                            font=('Arial', 15, 'underline', 'bold'))
        self.label6.place(x=50, y=130 , width=450)

        self.label6 = Label(self.root, text="Date de sortie: "+ ev.getDateSortie(),
                            font=('Arial', 15, 'underline', 'bold'))
        self.label6.place(x=50, y=170 , width=450)

        #####
        self.resumeFLM = Label(self.root, text="l'histoire du film:", font=("Andalus", 15,'underline', 'bold'), bg='white',
                               fg='black')
        self.resumeFLM.place(x=200, y=220)
        self.resume = Text(self.root, width=40, height=4)
        self.resume.insert(INSERT, ev.getResume())
        self.resume.config(font=('Arial', 15))
        self.resume.config(state="disabled")

        self.resume.place(x=50, y=250)
        self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.resume.yview)
        self.vsb.place(x=495, y=250, height=96)



obj=Detail_Film(root)
root.mainloop()