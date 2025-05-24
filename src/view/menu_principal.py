import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from controller.reservation_controller import ReservationController
from datetime import datetime

def launch_app():
    root = tk.Tk()
    app = MenuPrincipal(root, ReservationController())
    root.mainloop()

class MenuPrincipal:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("MeetingPro - Gestion des réservations")
        self.root.geometry("800x600")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        self.create_tabs()

    def create_tabs(self):
        self.create_ajouter_client_tab()
        self.create_ajouter_salle_tab()
        self.create_salles_reservables_tab()
        self.create_reservations_client_tab()
        self.create_disponibilite_salle_tab()
        self.create_salles_disponibles_tab()
        self.create_reserver_salle_tab()

    def create_ajouter_client_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Ajouter un client")
        tk.Label(tab, text="Nom").pack()
        self.nom_entry = tk.Entry(tab)
        self.nom_entry.pack()
        tk.Label(tab, text="Prénom").pack()
        self.prenom_entry = tk.Entry(tab)
        self.prenom_entry.pack()
        tk.Label(tab, text="Email").pack()
        self.email_entry = tk.Entry(tab)
        self.email_entry.pack()
        def valider():
            try:
                self.controller.ajouter_client(
                    self.nom_entry.get(), self.prenom_entry.get(), self.email_entry.get())
                messagebox.showinfo("Succès", "Client ajouté")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
        tk.Button(tab, text="Valider", command=valider).pack()

    def create_ajouter_salle_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Ajouter une salle")
        tk.Label(tab, text="Identifiant").pack()
        self.id_salle_entry = tk.Entry(tab)
        self.id_salle_entry.pack()
        tk.Label(tab, text="Type").pack()
        self.type_var = tk.StringVar(tab)
        self.type_var.set("Standard")
        tk.OptionMenu(tab, self.type_var, "Standard", "Conférence", "Informatique").pack()
        tk.Label(tab, text="Capacité").pack()
        self.capacite_entry = tk.Entry(tab)
        self.capacite_entry.pack()
        def valider():
            try:
                self.controller.ajouter_salle(
                    self.id_salle_entry.get(), self.type_var.get(), int(self.capacite_entry.get()))
                messagebox.showinfo("Succès", "Salle ajoutée")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
        tk.Button(tab, text="Valider", command=valider).pack()

    def create_salles_reservables_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Salles réservables")
        self.salle_listbox = tk.Listbox(tab)
        self.salle_listbox.pack(fill="both", expand=True)
        for salle in self.controller.salles:
            self.salle_listbox.insert(tk.END, f"{salle.identifiant} - {salle.type_salle} - {salle.capacite} places")

    def create_reservations_client_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Réservations client")
        def afficher():
            email = simpledialog.askstring("Email", "Email du client")
            if not email:
                return
            client = next((c for c in self.controller.clients if c.email == email), None)
            if client:
                reservations = [r for r in self.controller.reservations if r.client_id == client.id]
                info = ""
                for r in reservations:
                    salle = next((s for s in self.controller.salles if s.id == r.salle_id), None)
                    if salle:
                        info += f"Salle: {salle.identifiant}, Début: {r.date_debut}, Fin: {r.date_fin}\n"
                messagebox.showinfo("Réservations", info or "Aucune réservation")
            else:
                messagebox.showwarning("Erreur", "Client introuvable")
        tk.Button(tab, text="Voir les réservations", command=afficher).pack(pady=20)

    def create_disponibilite_salle_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Disponibilité salle")
        def verifier():
            nom_salle = simpledialog.askstring("Salle", "Identifiant de la salle")
            date_debut = simpledialog.askstring("Début", "Début (YYYY-MM-DD HH:MM)")
            date_fin = simpledialog.askstring("Fin", "Fin (YYYY-MM-DD HH:MM)")
            salle = next((s for s in self.controller.salles if s.identifiant == nom_salle), None)
            if salle:
                conflits = [r for r in self.controller.reservations if r.salle_id == salle.id and not (
                            date_fin <= r.date_debut or date_debut >= r.date_fin)]
                if not conflits:
                    messagebox.showinfo("Disponible", "Salle disponible")
                else:
                    messagebox.showwarning("Indisponible", "Salle non disponible à ce créneau")
            else:
                messagebox.showerror("Erreur", "Salle non trouvée")
        tk.Button(tab, text="Vérifier", command=verifier).pack(pady=20)

    def create_salles_disponibles_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Salles disponibles")
        def afficher():
            date_debut = simpledialog.askstring("Début", "Début (YYYY-MM-DD HH:MM)")
            date_fin = simpledialog.askstring("Fin", "Fin (YYYY-MM-DD HH:MM)")
            ids_res = [r.salle_id for r in self.controller.reservations
                       if not (date_fin <= r.date_debut or date_debut >= r.date_fin)]
            libres = [s.identifiant for s in self.controller.salles if s.id not in ids_res]
            messagebox.showinfo("Salles disponibles", "\n".join(libres) or "Aucune salle disponible")
        tk.Button(tab, text="Afficher", command=afficher).pack(pady=20)

    def create_reserver_salle_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Réserver une salle")
        tk.Label(tab, text="Email client").pack()
        self.email_client_res = tk.Entry(tab)
        self.email_client_res.pack()
        tk.Label(tab, text="Identifiant salle").pack()
        self.salle_id_res = tk.Entry(tab)
        self.salle_id_res.pack()
        tk.Label(tab, text="Début (YYYY-MM-DD HH:MM)").pack()
        self.date_debut_res = tk.Entry(tab)
        self.date_debut_res.pack()
        tk.Label(tab, text="Fin (YYYY-MM-DD HH:MM)").pack()
        self.date_fin_res = tk.Entry(tab)
        self.date_fin_res.pack()
        def reserver():
            try:
                client = next(c for c in self.controller.clients if c.email == self.email_client_res.get())
                salle = next(s for s in self.controller.salles if s.identifiant == self.salle_id_res.get())
                self.controller.reserver_salle(client.id, salle.id, self.date_debut_res.get(), self.date_fin_res.get())
                messagebox.showinfo("Réservé", "Réservation confirmée")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
        tk.Button(tab, text="Réserver", command=reserver).pack(pady=20)
