from user import User


class Client(User):

    def __init__(self):
        super().__init__()
        self.setDescription("Client")
