from user import User


class Employeur(User):

    def __init__(self):
        super().__init__()
        self.setDescription("Employeur")
