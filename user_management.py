import json
import os

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_user(name, roll):
    users = load_users()
    users.append({
        "name": name,
        "roll": roll,
        "image_folder": f"dataset/{name}_{roll}"
    })
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)