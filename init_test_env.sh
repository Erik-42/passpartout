#!/bin/bash

# Créer un environnement virtuel Python
python3 -m venv test_env

# Activer l'environnement
source test_env/bin/activate

# Installer les dépendances
pip install adafruit-circuitpython-hid
pip install adafruit-circuitpython-keyboard
pip install adafruit-circuitpython-mouse
pip install adafruit-circuitpython-consumercontrol

# Créer la structure de dossiers
mkdir -p test_env/{src,payloads,tests}

# Copier les fichiers nécessaires
rsync -av src/payloads/ test_env/payloads/
rsync -av tests/ test_env/tests/
rsync -av src/menu.py src/code.py src/payloads/__init__.py test_env/src/

# Créer le script de test principal dans le dossier src

# Créer un script de test principal
cat > test_env/run_tests.py << 'EOF'
import os
import sys
import time
import json
from typing import Dict, Any

# Ajouter le répertoire src au PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.menu import menus
from src.payloads import PayloadManager

class MockKeyboard:
    def __init__(self):
        self.keys_pressed = []

    def send(self, *keys):
        print(f"Appuyant sur les touches: {keys}")
        self.keys_pressed.extend(keys)

    def release_all(self):
        print("Libération de toutes les touches")
        self.keys_pressed.clear()

class MockMouse:
    def click(self, button):
        print(f"Clic sur le bouton {button}")

class MockConsumerControl:
    def send(self, code):
        codes = {
            96: "Volume down",
            97: "Volume mute",
            102: "Volume up"
        }
        print(f"Contrôle: {codes.get(code, 'Code inconnu')}")

class TestMenu:
    def __init__(self):
        self.keyboard = MockKeyboard()
        self.mouse = MockMouse()
        self.consumer_control = MockConsumerControl()
        self.payload_manager = PayloadManager()
        self.menu_stack = ['main']
        self.current_menu = self.get_menu('main')
        self.current_index = 0

    def get_menu(self, menu_name):
        return menus.get(menu_name, [])

    def show_menu(self):
        print("=== Menu Passpartout ===")
        print(f"\nMenu: {' -> '.join(self.menu_stack)}")
        print("\nOptions:")
        for i, option in enumerate(self.current_menu):
            if i == self.current_index:
                print(f">> {i + 1}. {option}")
            else:
                print(f"   {i + 1}. {option}")

    def handle_input(self, key):
        if key == 'up':
            self.current_index = max(0, self.current_index - 1)
        elif key == 'down':
            self.current_index = min(len(self.current_menu) - 1, self.current_index + 1)
        elif key == 'enter':
            self.select_option()
        elif key == 'back':
            self.go_back()

    def select_option(self):
        selected = self.current_menu[self.current_index]
        
        if selected in ['Windows', 'Linux', 'MacOS']:
            self.menu_stack.append(f"{selected.lower()}_payloads")
            self.current_menu = self.get_payloads_by_os(selected)
            self.current_index = 0
            return
            
        elif selected.endswith('.py') or selected.endswith('.json'):
            self.execute_payload(selected)
            return
            
        print(f"Option sélectionnée: {selected}")
        time.sleep(1)

    def get_payloads_by_os(self, os_name):
        payloads = []
        for payload in self.payload_manager.get_payloads():
            if payload.get('os') == os_name:
                payloads.append(payload['name'])
        return payloads

    def execute_payload(self, payload_name):
        print(f"\n=== Exécution du payload: {payload_name} ===")
        
        # Trouver l'ID du payload
        payload_id = payload_name[:-3] if payload_name.endswith('.py') else payload_name[:-5]
        
        # Exécuter le payload
        if not self.payload_manager.execute_payload(
            payload_id,
            keyboard=self.keyboard,
            mouse=self.mouse,
            consumer_control=self.consumer_control
        ):
            print("\nErreur lors de l'exécution du payload")
        
        input("\nAppuyez sur Entrée pour continuer...")

    def go_back(self):
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
            self.current_menu = self.get_menu(self.menu_stack[-1])
            self.current_index = 0

    def run(self):
        print("=== Test interactif Passpartout ===")
        print("Commandes:")
        print("↑/↓ : Navigation dans le menu")
        print("Enter : Sélectionner une option")
        print("B : Retourner au menu précédent")
        print("Q : Quitter")
        print("\nAppuyez sur une touche pour commencer...")

        while True:
            self.show_menu()
            
            key = input("\nChoisissez une option (↑/↓/Enter/B/Q): ").lower()
            
            if key == 'q':
                print("\nAu revoir!")
                break
                
            self.handle_input(key)

def main():
    test = TestMenu()
    test.run()

if __name__ == "__main__":
    main()
EOF

# Rendre le script exécutable
chmod +x test_env/run_tests.py

echo "\nEnvironnement de test initialisé avec succès !"
echo "Pour lancer les tests :"
echo "cd test_env && ./run_tests.py"

deactivate
