# 🧠 MeetingPro

**MeetingPro** est une application de gestion de réservation de salles, développée dans le cadre du module AOO à l’ENSISA.  
Elle permet de gérer efficacement les clients, les salles, les réservations et la disponibilité en temps réel, avec une interface moderne réalisée en `customtkinter`.

---

## 👥 Membres du projet

- **ABAGA NGUEMA Wayne Darky**
- **AGBO FAYEMI Doneck Florian**

---

## 🎯 Objectifs

> Concevoir une application modulaire Python (architecture MVC), avec persistance des données en JSON, gestion d’interactions utilisateurs via une interface graphique propre, tout en respectant les contraintes de robustesse, testabilité et expérience utilisateur.

---

## 🖥️ Fonctionnalités

- ✅ Ajouter un client avec contrôle d’unicité par e-mail
- ✅ Ajouter une salle avec type et capacité
- ✅ Réserver une salle avec gestion des conflits de créneaux
- ✅ Afficher toutes les salles disponibles pour un créneau donné
- ✅ Afficher les réservations d’un client
- ✅ Vérifier la disponibilité d’une salle pour un intervalle
- ✅ UI moderne et responsive (customtkinter) avec onglets et navigation fluide
- ✅ Enregistrement automatique des données dans `data.json`

---

## 🧱 Architecture du projet

```
MeetingPro/
├── src/
│   ├── main.py
│   ├── model/
│   ├── controller/
│   ├── view/
│   └── data.json
├── tests/
├── requirements.txt
└── README.md
```

---

## 🧪 Tests

Tous les tests sont réalisés avec `unittest` :
```bash
python -m unittest discover tests
```



## 🧰 Installation et exécution

1. Cloner le projet
```bash

git clone https://github.com/<votre-repo>
cd MeetingPro 
```

2. Installer les dépendances
```bash

pip install -r requirements.txt
```
Si customtkinter ne s’installe pas, faites :

```bash

pip install customtkinter
```

3. Lancer l'application
```bash

python src/main.py
```

## 🎨 UI - Aperçu
L’interface s’appuie sur `customtkinter` pour un design :

- Moderne (coins arrondis, fond clair/sombre)

- Fluide (navigation en onglets)

- Clair (champ par champ, avec feedback utilisateur)

- Inspiré des tendances actuelles de design flat/neumorphique



## 📁 Fichier de données
Toutes les données sont enregistrées dans un fichier `data.json` .
Aucune base de données externe n’est nécessaire.

## 📃 Rapport de projet
Un rapport PDF est disponible pour accompagner ce dépôt, incluant :

- Architecture

- Répartition des tâches

- Captures d’écran

- Problèmes rencontrés

- Retours sur expérience

## 📬 Contact
Pour toute question ou remarque :

wayne-darky.abaga-nguema@uha.fr

doneck-florian.agbo-fayemi@uha.fr
