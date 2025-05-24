import uuid

class Client:
    def __init__(self, nom, prenom, email, id=None):
        self.id = id or str(uuid.uuid4())
        self.nom = nom
        self.prenom = prenom
        self.email = email
