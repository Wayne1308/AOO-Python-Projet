import uuid

class Reservation:
    def __init__(self, client_id, salle_id, date_debut, date_fin, id=None):
        self.id = id or str(uuid.uuid4())
        self.client_id = client_id
        self.salle_id = salle_id
        self.date_debut = date_debut
        self.date_fin = date_fin
