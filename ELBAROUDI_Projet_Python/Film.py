

class Film(object):

    def __init__(self):
        self.idFilm = 0
        self.titre = None
        self.genre = None
        self.dure = None
        self.dateSortie = None
        self.resume = None


    # Getters
    def getIdFilm(self):
        return self.idFilm

    def getTitre(self):
        return self.titre

    def getGenre(self):
        return self.genre

    def getDure(self):
        return self.dure

    def getDateSortie(self):
        return self.dateSortie

    def getResume(self):
        return self.resume

    # Setters
    def setIdFilm(self, idFilm):
        self.idFilm = idFilm

    def setTitre(self, titre):
        self.titre = titre

    def setGenre(self, genre):
        self.genre = genre

    def setDure(self, dure):
        self.dure = dure

    def setDateSortie(self, dateSortie):
        self.dateSortie = dateSortie

    def setResume(self, resume):
        self.resume = resume


    # Get film By id
    def findFlBy(self, value, file_name='films.txt'):
        fileFilms = open('FilesTXT/' + file_name, 'r')
        for line in fileFilms:
            films = line.split(' ')
            if not self.getTitre():
                self.setTitre("")

            if films[0] == value or films[1].upper().replace('%L%', '\n').replace('&E&', ' ')==self.getTitre().upper():
             film = Film()
             film.setIdFilm(films[0])
             film.setTitre(films[1].replace('%L%', '\n').replace('&E&', ' '))
             film.setGenre(films[2].replace('%L%', '\n').replace('&E&', ' '))
             film.setDure(films[3].replace('%L%', '\n').replace('&E&', ' '))
             film.setDateSortie(films[4].replace('%L%', '\n').replace('&E&', ' '))
             film.setResume(films[5].replace('%L%', '\n').replace('&E&', ' '))
             return film

        fileFilms.close()
        return None


    # Get All films
    def findAllFl(self, file_name="films.txt"):
        Films = {}
        fileFilms = open('FilesTXT/' + file_name, 'r')
        i = 0
        for line in fileFilms:
            films = line.split(' ')

            film = Film()
            film.setIdFilm(films[0])
            film.setTitre(films[1].replace('%L%', '\n').replace('&E&', ' '))
            film.setGenre(films[2].replace('%L%', '\n').replace('&E&', ' '))
            film.setDure(films[3].replace('%L%', '\n').replace('&E&', ' '))
            film.setDateSortie(films[4].replace('%L%', '\n').replace('&E&', ' '))
            film.setResume(films[5].replace('%L%', '\n').replace('&E&', ' '))

            Films[i] = film

            i=i+1
        fileFilms.close()
        if Films == {}:
            return None
        return Films

    # ajouter un film
    def addFilm(self):
        try:
            fileFilms = open('FilesTXT/films.txt', 'r')
            for line in fileFilms:
                films = line.split(' ')

            idOfTheLastFilm =  int(films[0])
            idOfTheLastFilm += 1
            fileFilms.close()
            # Open a file with access mode 'a'
            fileFilms = open('FilesTXT/films.txt', 'a')
            # Append 'film' at the end of file
            fileFilms.write(str(idOfTheLastFilm) + ' ' + self.getTitre() + ' ' + self.getGenre() + ' ' + self.getDure() + ' ' + self.getDateSortie() + ' ' + self.getResume()+'\n')
            # Close the file
            fileFilms.close()
            return True
        except:
            return False

    # modifier les informations des dans le fichier films.txt
    def updateFilm(self):
        try:
            new_File_Content = ""
            fileFilms = open('FilesTXT/films.txt', 'r')
            for line in fileFilms:
                films = line.split(' ')
                if films[0] == self.getIdFilm():
                    new_File_Content += str(
                        self.getIdFilm()) + ' ' + self.getTitre() + ' ' + self.getGenre() + ' ' + self.getDure() + ' ' + self.getDateSortie() + ' ' + self.getResume().replace("\n","") + "\n"
                else:
                    new_File_Content += line
            fileFilms.close()

            writing_file = open("FilesTXT/films.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
            return False

    # supprimer un film
    def deleteFilm(self):
        try:
            # delete from the file films.txt
            new_File_Content = ""
            fileFilms = open('FilesTXT/films.txt', 'r')
            for line in fileFilms:
                films = line.split(' ')
                if films[0] != self.getIdFilm():
                    new_File_Content += line

            fileFilms.close()

            writing_file = open("FilesTXT/films.txt", "w")

            writing_file.write(new_File_Content)

            writing_file.close()

            return True
        except:
            return False








