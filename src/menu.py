import board
import digitalio
import time
import os
import json

# Mock pour le module storage
class MockStorage:
    def disable_usb_drive(self):
        print("Lecteur USB désactivé")
    
storage = MockStorage()
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Configuration des boutons
up_btn = digitalio.DigitalInOut(board.GP15)
down_btn = digitalio.DigitalInOut(board.GP14)
select_btn = digitalio.DigitalInOut(board.GP13)
back_btn = digitalio.DigitalInOut(board.GP12)

# Initialisation des boutons
for btn in [up_btn, down_btn, select_btn, back_btn]:
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

# Configuration du clavier
kb = Keyboard()
layout = KeyboardLayoutUS(kb)

# Variables globales
current_menu = "main"
menu_position = 0
config = {}

# Menus disponibles
from payloads import load_payloads

# Charger les payloads au démarrage
payload_manager = load_payloads()

menus = {
    "main": [
        "Système d'exploitation",
        "Séquences de dépannage",
        "Payloads",
        "Options d'exécution",
        "Sauvegarder",
        "Exécuter"
    ],
    "os": [
        "Windows",
        "Linux",
        "MacOS",
        "Version...",
        "Paramètres régionaux..."
    ],
    "sequences": [
        "Mode de récupération",
        "Déblocage utilisateur",
        "Commandes système",
        "Commandes Mac spécifiques",
        "Personnaliser..."
    ],
    "options": [
        "Messages de confirmation",
        "Délais...",
        "Combinaisons de touches..."
    ],
    "mac_commands": [
        "Commande + Option + R (récupération)",
        "Commande + Option + P + R (réinitialisation PRAM)",
        "Commande + Option + Shift + R (récupération mise à jour)",
        "Commande + R (récupération rapide)",
        "Commande + Shift (démarrage en mode sans échec)",
        "Commande + Option + Esc (force quit)",
        "Commande + Option + D (dock)",
        "Commande + Option + M (mission control)",
        "Commande + Option + Espace (Spotlight)",
        "Commande + Option + F2 (mode développeur)"
    ],
    "payloads": [
        "Windows",
        "Linux",
        "MacOS"
    ],
    "windows_payloads": [
        f"{payload['name']}" for payload in payload_manager.get_payloads_by_os("Windows")
    ],
    "linux_payloads": [
        f"{payload['name']}" for payload in payload_manager.get_payloads_by_os("Linux")
    ],
    "mac_payloads": [
        f"{payload['name']}" for payload in payload_manager.get_payloads_by_os("MacOS")
    ]
}

def load_config():
    """Charge la configuration depuis le fichier"""
    global config
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except:
        config = {}

def save_config():
    """Sauvegarde la configuration"""
    with open("config.json", "w") as f:
        json.dump(config, f)

def display_menu():
    """Affiche le menu actuel"""
    menu_items = menus[current_menu]
    for i, item in enumerate(menu_items):
        if i == menu_position:
            layout.write(f"> {item}\n")
        else:
            layout.write(f"  {item}\n")
    layout.write("\n")

def handle_input():
    """Gère les entrées utilisateur"""
    global menu_position, current_menu
    
    if not up_btn.value:  # Bouton haut
        menu_position = max(0, menu_position - 1)
        time.sleep(0.2)
        return True
    
    if not down_btn.value:  # Bouton bas
        menu_position = min(len(menus[current_menu]) - 1, menu_position + 1)
        time.sleep(0.2)
        return True
    
    if not select_btn.value:  # Bouton sélection
        selected_item = menus[current_menu][menu_position]
        if current_menu == "main":
            if selected_item == "Système d'exploitation":
                current_menu = "os"
            elif selected_item == "Séquences de dépannage":
                current_menu = "sequences"
            elif selected_item == "Options d'exécution":
                current_menu = "options"
            elif selected_item == "Sauvegarder":
                save_config()
            elif selected_item == "Exécuter":
                return False  # Quitte le menu
        time.sleep(0.2)
        return True
    
    if not back_btn.value:  # Bouton retour
        current_menu = "main"
        menu_position = 0
        time.sleep(0.2)
        return True
    
    return True

def main():
    """Fonction principale du menu"""
    load_config()
    
    while True:
        display_menu()
        if not handle_input():
            break

if __name__ == "__main__":
    main()
