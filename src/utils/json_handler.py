# Utilitaire de lecture/écriture JSON
import json
import os

def load_data(file_path='data.json'):
    if not os.path.exists(file_path):
        return {"clients": [], "salles": [], "reservations": []}
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(data, file_path='data.json'):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)