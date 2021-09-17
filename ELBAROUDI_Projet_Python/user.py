import sys


class User(object):

    def __init__(self):
        self.idUser =0
        self.nom =None
        self.prenom =None
        self.numTele =None
        self.description =None
        self.NomduCompte =None
        self.password =None
        self.verified =None

    #Getters
    def getIdUser(self):
        return self.idUser

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getNumTele(self):
        return self.numTele

    def getDescription(self):
        return self.description

    def getNomducompte(self):
        return self.NomduCompte

    def getPassword(self):
        return self.password

    def getVerified(self):
        return self.verified

    #Setters
    def setIdUser(self, idUser):
        self.idUser = idUser

    def setNom(self,nom):
        self.nom=nom

    def setPrenom(self,prenom):
        self.prenom=prenom

    def setNumTele(self,numTele):
        self.numTele=numTele

    def setDescription(self,description):
        self.description=description

    def setNomducompte(self,NomduCompte):
        self.NomduCompte=NomduCompte

    def setPassword(self,password):
        self.password=password

    def setVerified(self,verified):
        self.verified=verified

    # Get User
    def findUsBy(self, file_name = 'users.txt'):
        fileUsers = open('FilesTXT/'+file_name, 'r')
        for line in fileUsers:
            user = line.split(' ')
            if user[5].upper()==self.getNomducompte().upper() or user[3]==self.getNumTele():
                sys.path.append(".")
                if user[4]=="Admin":
                    from Admin import Admin
                    utilisateur = Admin()
                elif user[4]=="Client":
                     from Client import Client
                     utilisateur = Client()
                elif user[4]=="Employeur":
                     from Employeur import Employeur
                     utilisateur = Employeur()

                utilisateur.setIdUser(user[0])
                utilisateur.setNom(user[1])
                utilisateur.setPrenom(user[2])
                utilisateur.setNumTele(user[3])
                utilisateur.setDescription(user[4])
                utilisateur.setNomducompte(user[5])
                utilisateur.setPassword(user[6])
                utilisateur.setVerified(user[7])

                return utilisateur
        fileUsers.close()
        return False

    # Get All users
    def findAllUS(self,file_name="users.txt"):
        Users= {}
        fileUsers = open('FilesTXT/' + file_name, 'r')
        i=0
        for line in fileUsers:
            user = line.split(' ')
            sys.path.append(".")

            if user[4] == "Admin":
                from Admin import Admin
                utilisateur = Admin()
            elif user[4] == "Client":
                from Client import Client
                utilisateur = Client()
            elif user[4] == "Employeur":
                from Employeur import Employeur
                utilisateur = Employeur()

            utilisateur.setIdUser(user[0])
            utilisateur.setNom(user[1])
            utilisateur.setPrenom(user[2])
            utilisateur.setNumTele(user[3])
            utilisateur.setNomducompte(user[5])
            utilisateur.setPassword(user[6])
            utilisateur.setVerified(user[7])

            Users[i]=utilisateur

            i+=1

        fileUsers.close()
        if Users=={}:
            return None
        return Users
    #ajouter un utilisateur
    def addUser(self):
        try:
            file_user = open('FilesTXT/users.txt', 'r')
            for line in file_user:
                user = line.split(' ')
            idOfTheLastUser= int(user[0])
            idOfTheLastUser+=1
            file_user.close()

            # Open a file with access mode 'a'
            file_user = open('FilesTXT/users.txt', 'a')
            # Append 'user' at the end of file
            file_user.write(str(idOfTheLastUser)+' '+self.getNom()+' '+self.getPrenom()+' '+self.getNumTele()+' '+self.getDescription()+' '+self.getNomducompte()+' '+self.getPassword()+' '+self.getVerified()+"\n")
            # Close the file
            file_user.close()
            return True
        except:
            return False
    #modifier les informations des utilisateurs
    def updateUser(self):
        try:
            new_File_Content=""
            file_user = open('FilesTXT/users.txt', 'r')
            for line in file_user:
                user = line.split(' ')
                if user[0]==str(self.getIdUser()):
                    new_File_Content+=str(self.getIdUser())+' '+self.getNom()+' '+self.getPrenom()+' '+self.getNumTele()+' '+self.getDescription()+' '+self.getNomducompte()+' '+self.getPassword()+' '+self.getVerified().replace("\n","")+"\n"
                else:
                    new_File_Content+=line
            file_user.close()

            writing_file = open("FilesTXT/users.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
                return False
    #supprimer un utilisateur
    def deleteUser(self):
        try:
            # delete from the file of description user
            new_File_Content = ""
            file_user = open('FilesTXT/users.txt', 'r')
            for line in file_user:
                user = line.split(' ')
                if user[0] != self.getIdUser():
                    new_File_Content += line

            file_user.close()

            writing_file = open("FilesTXT/users.txt", "w")
            writing_file.write(new_File_Content)
            writing_file.close()

            #delete from the user file
            new_File_Content=""
            file_user = open('FilesTXT/users.txt', 'r')
            for line in file_user:
                user = line.split(' ')
                if user[0]!=self.getIdUser():
                    new_File_Content+=line

            file_user.close()

            writing_file = open("FilesTXT/users.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()


            return True
        except:
                return False
    #gerer la demande d'inscription des utilisateurs
    def gerer_demande(self,verf):
        try:
            new_File_Content=""
            file_user = open('FilesTXT/users.txt', 'r')
            for line in file_user:
                user = line.split(' ')
                if user[0]==self.getIdUser():
                    new_File_Content+=str(self.getIdUser())+' '+user[1]+' '+user[2]+' '+user[3]+' '+user[4]+' '+user[5]+' '+user[6]+' '+verf+"\n"
                else:
                    new_File_Content+=line



            file_user.close()

            writing_file = open("FilesTXT/users.txt", "w")
            writing_file.write(new_File_Content)
            writing_file.close()

            return True
        except:
            return False
   









