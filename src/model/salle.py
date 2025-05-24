import uuid

class Salle:
    def __init__(self, identifiant, type_salle, capacite, id=None):
        self.id = id or str(uuid.uuid4())
        self.identifiant = identifiant
        self.type_salle = type_salle
        self.capacite = capacite
