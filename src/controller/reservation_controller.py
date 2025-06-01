from model.client import Client
from model.salle import Salle
from model.reservation import Reservation
from utils.json_handler import load_data, save_data
from datetime import datetime

class ReservationController:
    def __init__(self):
        data = load_data()
        self.clients = [Client(**c) for c in data.get("clients", [])]
        self.salles = [Salle(**s) for s in data.get("salles", [])]
        self.reservations = [
            Reservation(
                r["client_id"],
                r["salle_id"],
                datetime.strptime(r["date_debut"], "%Y-%m-%d %H:%M"),
                datetime.strptime(r["date_fin"], "%Y-%m-%d %H:%M"),
                id=r.get("id")
            )
            for r in data.get("reservations", [])
        ]

    def save(self):
        data = {
            "clients": [vars(c) for c in self.clients],
            "salles": [vars(s) for s in self.salles],
            "reservations": [
                {
                    "id": r.id,
                    "client_id": r.client_id,
                    "salle_id": r.salle_id,
                    "date_debut": r.date_debut.strftime("%Y-%m-%d %H:%M") if isinstance(r.date_debut, datetime) else r.date_debut,
                    "date_fin": r.date_fin.strftime("%Y-%m-%d %H:%M") if isinstance(r.date_fin, datetime) else r.date_fin
                }
                for r in self.reservations
            ]
        }
        save_data(data)

    def ajouter_client(self, nom, prenom, email):
        if any(c.email == email for c in self.clients):
            raise ValueError("Email déjà utilisé.")
        client = Client(nom, prenom, email)
        self.clients.append(client)
        self.save()

    def ajouter_salle(self, identifiant, type_salle, capacite):
        if any(s.identifiant == identifiant for s in self.salles):
            raise ValueError("Identifiant déjà utilisé.")
        salle = Salle(identifiant, type_salle, capacite)
        self.salles.append(salle)
        self.save()

    def reserver_salle(self, client_id, salle_id, date_debut, date_fin):
        if any(r.salle_id == salle_id and not (date_fin <= r.date_debut or date_debut >= r.date_fin)
               for r in self.reservations):
            raise ValueError("Salle non disponible pour ce créneau.")
        reservation = Reservation(client_id, salle_id, date_debut, date_fin)
        self.reservations.append(reservation)
        self.save()
        return reservation
