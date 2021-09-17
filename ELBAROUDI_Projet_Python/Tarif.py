

class Tarif(object):

    def __init__(self):
        self.idTarif = 0
        self.categorie = None
        self.cout = 0


    # Getters
    def getIdTarif(self):
        return self.idTarif

    def getCategorie(self):
        return self.categorie

    def getCout(self):
        return self.cout


    # Setters
    def setIdTarif(self, idTarif):
        self.idTarif = idTarif

    def setCategorie(self, categorie):
        self.categorie = categorie

    def setCout(self, cout):
        self.cout = cout


    # Get Tarif By id
    def findTrBy(self, value, file_name='Tarif.txt'):
        fileTarif = open('FilesTXT/' + file_name, 'r')
        for line in fileTarif:
            Tarifs = line.split(' ')
            if Tarifs[0] == value:
             tarif = Tarif()
             tarif.setIdTarif(Tarifs[0])
             tarif.setCategorie(Tarifs[1])
             tarif.setCout(Tarifs[2])

             return tarif

        fileTarif.close()
        return None


    # Get All Tarif
    def finAllTr(self, file_name="Tarif.txt"):
        TARIFS = {}
        fileTarif = open('FilesTXT/' + file_name, 'r')
        i = 0
        for line in fileTarif:
            atr_Tarifs = line.split(' ')

            tarif = Tarif()
            tarif.setIdTarif(atr_Tarifs[0])
            tarif.setCategorie(atr_Tarifs[1])
            tarif.setCout(atr_Tarifs[2])

            TARIFS[i] = tarif
            i=i+1
        fileTarif.close()
        if TARIFS == {}:
            return None
        return TARIFS


    # modifier un Tarif
    def updateTarif(self):
        try:
            new_File_Content = ""
            fileTarif = open('FilesTXT/Tarif.txt', 'r')
            for line in fileTarif:
                Tarifs = line.split(' ')
                if Tarifs[0] == self.getIdTarif():
                    new_File_Content += str(self.getIdTarif())+' '+self.getCategorie()+' '+str(self.getCout().replace("\n",""))+"\n"
                else:
                    new_File_Content += line
            fileTarif.close()

            writing_file = open("FilesTXT/Tarif.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
            return False








