from user import User


class Admin(User):

    def __init__(self):
        super().__init__()
        self.setDescription("Admin")
