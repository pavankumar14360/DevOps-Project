class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        # Logic to save the user to a database or file
        pass

    def load(self, username):
        # Logic to load a user from a database or file
        pass