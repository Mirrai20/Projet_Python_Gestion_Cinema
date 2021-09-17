

class Salle(object):

    def __init__(self):
        self.idSalle = 0
        self.numSalle = 0
        self.description = None
        self.capacite = 0


    # Getters
    def getIdSalle(self):
        return self.idSalle

    def getNumSalle(self):
        return self.numSalle

    def getDescription(self):
        return self.description

    def getCapacite(self):
        return self.capacite

    # Setters
    def setIdSalle(self, idSalle):
        self.idSalle = idSalle

    def setNumSalle(self, numSalle):
        self.numSalle = numSalle

    def setDescription(self, description):
        self.description = description

    def setCapacite(self, capacite):
        self.capacite = capacite

    # Get Salle By id
    def findSlBy(self, value, file_name='Salles.txt'):
        if not self.getNumSalle():
            self.setNumSalle("")

        fileSalles = open('FilesTXT/' + file_name, 'r')

        for line in fileSalles:
            Salles = line.split(' ')
            if Salles[0] == value or Salles[1]==self.getNumSalle():
             salle = Salle()
             salle.setIdSalle(Salles[0])
             salle.setNumSalle(Salles[1].replace('%L%', '\n').replace('&E&', ' '))
             salle.setDescription(Salles[2].replace('%L%', '\n').replace('&E&', ' '))
             salle.setCapacite(Salles[3].replace('%L%', '\n').replace('&E&', ' '))

             return salle

        fileSalles.close()
        return None


    # Get All Salles
    def findAllSl(self, file_name="Salles.txt"):
        Salles = {}
        fileSalles = open('FilesTXT/' + file_name, 'r')
        i = 0
        for line in fileSalles:
            atr_salle = line.split(' ')

            salle = Salle()
            salle.setIdSalle(atr_salle[0])
            salle.setNumSalle(atr_salle[1].replace('%L%', '\n').replace('&E&', ' '))
            salle.setDescription(atr_salle[2].replace('%L%', '\n').replace('&E&', ' '))
            salle.setCapacite(atr_salle[3].replace('%L%', '\n').replace('&E&', ' '))

            Salles[i] = salle
            i=i+1
        fileSalles.close()
        if Salles == {}:
            return None
        return Salles

    # ajouter une salle
    def addSalle(self):
        try:
            fileSalles = open('FilesTXT/Salles.txt', 'r')
            for line in fileSalles:
                salles = line.split(' ')

            idOfTheLastSalle = int(salles[0])
            idOfTheLastSalle += 1
            fileSalles.close()
            # Open a file with access mode 'a'
            fileSalles = open('FilesTXT/Salles.txt', 'a')
            # Append 'salle' at the end of file
            fileSalles.write(str(idOfTheLastSalle) + ' ' + str(self.getNumSalle()) + ' ' + self.getDescription() + ' ' + str(self.getCapacite())+'\n')
            # Close the file
            fileSalles.close()
            return True
        except:
            return False

    # modifier les informations des dans le fichier Salles.txt
    def updateSalle(self):
        try:
            new_File_Content = ""
            fileSalles = open('FilesTXT/Salles.txt', 'r')
            for line in fileSalles:
                Salles = line.split(' ')
                if Salles[0] == self.getIdSalle():
                    new_File_Content += str(self.getIdSalle()) + ' ' + str(self.getNumSalle()) + ' ' + self.getDescription() + ' ' + str(self.getCapacite()).replace("\n","")+"\n"
                else:
                    new_File_Content += line
            fileSalles.close()

            writing_file = open("FilesTXT/Salles.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
            return False

    # supprimer une salle
    def deleteSalle(self):
        try:
            # delete from the file Salles.txt
            new_File_Content = ""
            fileSalles = open('FilesTXT/Salles.txt', 'r')
            for line in fileSalles:
                Salles = line.split(' ')
                if Salles[0] != self.getIdSalle():
                    new_File_Content += line

            fileSalles.close()

            writing_file = open("FilesTXT/Salles.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
            return False








