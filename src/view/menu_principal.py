import customtkinter as ctk
from tkinter import messagebox, simpledialog
from controller.reservation_controller import ReservationController
from datetime import datetime

ctk.set_appearance_mode("System")  # "Dark" or "Light"
ctk.set_default_color_theme("blue")

class MenuPrincipal(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("MeetingPro - Gestion des réservations")
        self.geometry("1000x700")
        self.configure(bg="#f4f4f4")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="MeetingPro", font=("Segoe UI", 28, "bold"))
        self.title_label.grid(row=0, column=0, pady=20)

        self.tabview = ctk.CTkTabview(self, corner_radius=15, width=800, height=600)
        self.tabview.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.create_tabs()

    def create_tabs(self):
        self.accueil_tab = self.tabview.add("Accueil")
        self.ajouter_client_tab = self.tabview.add("Ajouter un client")
        self.ajouter_salle_tab = self.tabview.add("Ajouter une salle")
        self.reserver_tab = self.tabview.add("Réserver")
        self.afficher_clients_tab = self.tabview.add("Afficher Clients")
        self.afficher_salles_tab = self.tabview.add("Afficher Salles")
        self.reservations_client_tab = self.tabview.add("Réservations client")
        self.salles_dispo_tab = self.tabview.add("Salles disponibles")

        self.init_accueil()
        self.init_ajouter_client()
        self.init_ajouter_salle()
        self.init_reserver()
        self.init_afficher_clients()
        self.init_afficher_salles()
        self.init_reservations_client()
        self.init_salles_dispo()

    def init_accueil(self):
        ctk.CTkLabel(self.accueil_tab, text="Bienvenue dans MeetingPro", font=("Segoe UI", 18)).pack(pady=30)

    def init_ajouter_client(self):
        frame = ctk.CTkFrame(self.ajouter_client_tab, corner_radius=12)
        frame.pack(pady=40)

        self.client_entries = {}
        for field in ["Nom", "Prénom", "Email"]:
            ctk.CTkLabel(frame, text=field).pack(pady=(10, 0))
            entry = ctk.CTkEntry(frame, width=300, corner_radius=10)
            entry.pack(pady=5)
            self.client_entries[field] = entry

        def valider():
            try:
                nom = self.client_entries["Nom"].get()
                prenom = self.client_entries["Prénom"].get()
                email = self.client_entries["Email"].get()
                self.controller.ajouter_client(nom, prenom, email)
                messagebox.showinfo("Succès", "Client ajouté")
                self.tabview.set("Accueil")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        def annuler():
            for entry in self.client_entries.values():
                entry.delete(0, "end")

        ctk.CTkButton(frame, text="Valider", command=valider, corner_radius=10).pack(pady=10)
        ctk.CTkButton(frame, text="Annuler", command=annuler, fg_color="gray", corner_radius=10).pack()

    def init_ajouter_salle(self):
        frame = ctk.CTkFrame(self.ajouter_salle_tab, corner_radius=12)
        frame.pack(pady=40)

        self.id_entry = ctk.CTkEntry(frame, placeholder_text="Identifiant", width=300)
        self.id_entry.pack(pady=5)

        self.type_box = ctk.CTkOptionMenu(frame, values=["Standard", "Conférence", "Informatique"])
        self.type_box.pack(pady=5)

        self.capacite_entry = ctk.CTkEntry(frame, placeholder_text="Capacité", width=300)
        self.capacite_entry.pack(pady=5)

        def valider():
            try:
                self.controller.ajouter_salle(
                    self.id_entry.get(), self.type_box.get(), int(self.capacite_entry.get())
                )
                messagebox.showinfo("Succès", "Salle ajoutée")
                self.tabview.set("Accueil")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        ctk.CTkButton(frame, text="Ajouter", command=valider).pack(pady=10)

    def init_reserver(self):
        frame = ctk.CTkFrame(self.reserver_tab, corner_radius=12)
        frame.pack(pady=40)

        self.res_inputs = {}
        for champ in ["Email client", "Identifiant salle", "Début (YYYY-MM-DD HH:MM)", "Fin (YYYY-MM-DD HH:MM)"]:
            ctk.CTkLabel(frame, text=champ).pack(pady=(10, 0))
            entry = ctk.CTkEntry(frame, width=300)
            entry.pack(pady=5)
            self.res_inputs[champ] = entry

        def reserver():
            try:
                email = self.res_inputs["Email client"].get()
                salle_id = self.res_inputs["Identifiant salle"].get()
                debut = datetime.strptime(self.res_inputs["Début (YYYY-MM-DD HH:MM)"].get(), "%Y-%m-%d %H:%M")
                fin = datetime.strptime(self.res_inputs["Fin (YYYY-MM-DD HH:MM)"].get(), "%Y-%m-%d %H:%M")
                client = next(c for c in self.controller.clients if c.email == email)
                salle = next(s for s in self.controller.salles if s.identifiant == salle_id)
                self.controller.reserver_salle(client.id, salle.id, debut, fin)
                messagebox.showinfo("Réservation", "Réservation effectuée")
                self.tabview.set("Accueil")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        ctk.CTkButton(frame, text="Réserver", command=reserver).pack(pady=10)

    def init_afficher_clients(self):
        box = ctk.CTkTextbox(self.afficher_clients_tab, width=800, height=500)
        box.pack(padx=20, pady=20)
        for c in self.controller.clients:
            box.insert("end", f"{c.nom} {c.prenom} - {c.email}\n")

    def init_afficher_salles(self):
        box = ctk.CTkTextbox(self.afficher_salles_tab, width=800, height=500)
        box.pack(padx=20, pady=20)
        for s in self.controller.salles:
            box.insert("end", f"{s.identifiant} - {s.type_salle} ({s.capacite} places)\n")

    def init_reservations_client(self):
        def afficher():
            email = simpledialog.askstring("Email", "Email du client")
            if not email:
                return
            client = next((c for c in self.controller.clients if c.email == email), None)
            if not client:
                messagebox.showwarning("Erreur", "Client non trouvé")
                return
            reservations = [r for r in self.controller.reservations if r.client_id == client.id]
            infos = "\n".join([
                f"Salle: {next((s.identifiant for s in self.controller.salles if s.id == r.salle_id), '?')}, Début: {r.date_debut}, Fin: {r.date_fin}" for r in reservations])
            messagebox.showinfo("Réservations", infos or "Aucune réservation")

        ctk.CTkButton(self.reservations_client_tab, text="Voir les réservations", command=afficher).pack(pady=30)

    def init_salles_dispo(self):
        def afficher():
            debut = simpledialog.askstring("Début", "Début (YYYY-MM-DD HH:MM)")
            fin = simpledialog.askstring("Fin", "Fin (YYYY-MM-DD HH:MM)")
            try:
                d1 = datetime.strptime(debut, "%Y-%m-%d %H:%M")
                d2 = datetime.strptime(fin, "%Y-%m-%d %H:%M")
                ids = [r.salle_id for r in self.controller.reservations if not (d2 <= r.date_debut or d1 >= r.date_fin)]
                libres = [s.identifiant for s in self.controller.salles if s.id not in ids]
                messagebox.showinfo("Disponibles", "\n".join(libres) or "Aucune salle libre")
            except:
                messagebox.showerror("Erreur", "Format invalide")

        ctk.CTkButton(self.salles_dispo_tab, text="Afficher", command=afficher).pack(pady=30)


def launch_app():
    controller = ReservationController()
    app = MenuPrincipal(controller)
    app.mainloop()

if __name__ == '__main__':
    launch_app()
