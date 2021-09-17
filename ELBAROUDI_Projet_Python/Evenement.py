from tkinter import messagebox

from Film import Film
from Salle import Salle
from Tarif import Tarif


class Evenement(Film,Salle,Tarif):

    def __init__(self):
        self.idevenement = 0
        Film.__init__(self)
        Salle.__init__(self)
        Tarif.__init__(self)
        self.dateDiffusion = None
        self.jourDiffusion = None
        self.nbPlaceReserver = 0


    # Getters
    def getIDevenement(self):
        return self.idevenement

    def getDateDiffusion(self):
        return self.dateDiffusion

    def getJourDiffusion(self):
        return self.jourDiffusion

    def getNbPlaceReserver(self):
        return self.nbPlaceReserver

    # Setters
    def setIDevenement(self, idevenement):
        self.idevenement = idevenement

    def setDateDiffusion(self, dateDiffusion):
        self.dateDiffusion = dateDiffusion

    def setJourDiffusion(self, jourDiffusion):
        self.jourDiffusion = jourDiffusion

    def setNbPlaceReserver(self, nbPlaceReserver):
        self.nbPlaceReserver = nbPlaceReserver


    # Get evenement By id
    def findEvBy(self, value, file_name='Evenements.txt'):
        fileEvenements = open('FilesTXT/' + file_name, 'r')
        for line in fileEvenements:
            evenements = line.split(' ')
            if evenements[0] == value:
             evenement = Evenement()
             if evenement.findFlBy(evenements[1]) == None:
                 messagebox.showerror("WARNING", "Movie NOT FOUND")
                 return False

             if evenement.findSlBy(evenements[2])== None:
                 messagebox.showerror("WARNING", "Salle NOT FOUND")
                 return False

             if evenement.findTrBy(evenements[3])== None:
                 messagebox.showerror("WARNING", "Tarif NOT FOUND")
                 return False

             # Evenement
             evenement.setIDevenement(evenements[0])
             evenement.setIdFilm(evenements[1])
             evenement.setIdSalle(evenements[2])
             evenement.setIdTarif(evenements[3])
             evenement.setDateDiffusion(evenements[4].replace('%L%', '\n').replace('&E&', ' '))
             evenement.setJourDiffusion(evenements[5].replace('%L%', '\n').replace('&E&', ' '))
             evenement.setNbPlaceReserver(evenements[6].replace('%L%', '\n').replace('&E&', ' '))
             # FILM
             evenement.setTitre(evenement.findFlBy(evenements[1]).getTitre())
             evenement.setGenre(evenement.findFlBy(evenements[1]).getGenre())
             evenement.setDure(evenement.findFlBy(evenements[1]).getDure())
             evenement.setDateSortie(evenement.findFlBy(evenements[1]).getDateSortie())
             evenement.setResume(evenement.findFlBy(evenements[1]).getResume())
             # SALLE
             evenement.setNumSalle(evenement.findSlBy(evenements[2]).getNumSalle())
             evenement.setDescription(evenement.findSlBy(evenements[2]).getDescription())
             evenement.setCapacite(evenement.findSlBy(evenements[2]).getCapacite())
             # TARIF
             evenement.setCategorie(evenement.findTrBy(evenements[3]).getCategorie())
             evenement.setCout(evenement.findTrBy(evenements[3]).getCout())
             return evenement

        fileEvenements.close()
        return None


    # Get All Evenement
    def findAllEv(self, file_name="Evenements.txt"):
        Evenements = {}
        fileEvenements = open('FilesTXT/' + file_name, 'r')
        i = 0
        for line in fileEvenements:
            atr_evenement = line.split(' ')
            evenement = Evenement()
            if evenement.findFlBy(atr_evenement[1]) == None:
                messagebox.showerror("WARNING", "Movie NOT FOUND")
                return False

            if evenement.findSlBy(atr_evenement[2]) == None:
                messagebox.showerror("WARNING", "Salle NOT FOUND")
                return False

            if evenement.findTrBy(atr_evenement[3]) == None:
                messagebox.showerror("WARNING", "Tarif NOT FOUND")
                return False
            #Evenement
            evenement.setIDevenement(atr_evenement[0])
            evenement.setIdFilm(atr_evenement[1])
            evenement.setIdSalle(atr_evenement[2])
            evenement.setIdTarif(atr_evenement[3])
            evenement.setDateDiffusion(atr_evenement[4].replace('%L%', '\n').replace('&E&', ' '))
            evenement.setJourDiffusion(atr_evenement[5].replace('%L%', '\n').replace('&E&', ' '))
            evenement.setNbPlaceReserver(atr_evenement[6].replace('%L%', '\n').replace('&E&', ' '))
            #FILM
            evenement.setTitre(evenement.findFlBy(atr_evenement[1]).getTitre())
            evenement.setGenre(evenement.findFlBy(atr_evenement[1]).getGenre())
            evenement.setDure(evenement.findFlBy(atr_evenement[1]).getDure())
            evenement.setDateSortie(evenement.findFlBy(atr_evenement[1]).getDateSortie())
            evenement.setResume(evenement.findFlBy(atr_evenement[1]).getResume())
            #SALLE
            evenement.setNumSalle(evenement.findSlBy(atr_evenement[2]).getNumSalle())
            evenement.setDescription(evenement.findSlBy(atr_evenement[2]).getDescription())
            evenement.setCapacite(evenement.findSlBy(atr_evenement[2]).getCapacite())
            #TARIF
            evenement.setCategorie(evenement.findTrBy(atr_evenement[3]).getCategorie())
            evenement.setCout(evenement.findTrBy(atr_evenement[3]).getCout())


            Evenements[i] = evenement
            i+=1
        fileEvenements.close()
        if Evenements == {}:
            return None
        return Evenements

    # ajouter un Evenement
    def addEvenement(self):
        try:
            fileEvenements = open('FilesTXT/Evenements.txt', 'r')
            for line in fileEvenements:
                evenements = line.split(' ')

            idOfTheLastEv =  int(evenements[0])
            idOfTheLastEv += 1
            fileEvenements.close()

            # Open a file with access mode 'a'
            fileEvenements = open('FilesTXT/Evenements.txt', 'a')
            # Append 'evenement' at the end of file
            fileEvenements.write(str(idOfTheLastEv) + ' ' + str(self.getIdFilm()) + ' ' + str(self.getIdSalle()) + ' ' + str(self.getIdTarif()) + ' ' + self.getDateDiffusion() + ' '+ str(self.getJourDiffusion())+' '+ str(self.getNbPlaceReserver())+"\n")
            # Close the file
            fileEvenements.close()



            return True
        except:
            return False

    # modifier un evenement
    def updateEvenement(self):
        try:
            new_File_Content = ""
            fileEvenements = open('FilesTXT/Evenements.txt', 'r')
            for line in fileEvenements:
                evenements = line.split(' ')
                if evenements[0] == self.getIDevenement():
                    new_File_Content +=  str(self.getIDevenement())+' '+ str(self.getIdFilm()) + ' ' + str(self.getIdSalle()) + ' ' + str(self.getIdTarif()) + ' ' + self.getDateDiffusion()+' '+ self.getJourDiffusion() + ' ' + str(self.getNbPlaceReserver()).replace("\n","")+"\n"
                else:
                    new_File_Content += line
            fileEvenements.close()

            writing_file = open("FilesTXT/Evenements.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
            return False

    # supprimer un evenement
    def deleteEvenement(self):
        try:
            # delete from the file Evenements.txt
            new_File_Content = ""
            fileEvenements = open('FilesTXT/Evenements.txt', 'r')
            for line in fileEvenements:
                evenements = line.split(' ')
                if evenements[0] != self.getIDevenement():
                    new_File_Content += line

            fileEvenements.close()

            writing_file = open("FilesTXT/Evenements.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
            return False








