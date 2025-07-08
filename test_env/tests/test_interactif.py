import os
import sys
import time
from typing import Dict, Any
import json
import random

# Ajouter le répertoire parent au PATH pour les imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Remplacer les imports par les mocks
from mock_hardware import create_hardware
from mock_storage import storage
from src.payloads import PayloadManager
from src.menu import menus

class TestInteractif:
    """Test interactif du projet Passpartout"""
    
    def __init__(self):
        self.hardware = create_hardware()
        self.payload_manager = PayloadManager()
        self.menu_stack = ['main']
        self.current_menu = menus['main']
        self.current_index = 0
        
    def clear_screen(self):
        """Efface l'écran"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def show_menu(self):
        """Affiche le menu actuel"""
        self.clear_screen()
        print("=== Menu Passpartout ===")
        print(f"\nMenu: {' -> '.join(self.menu_stack)}")
        print("\nOptions:")
        for i, option in enumerate(self.current_menu):
            if i == self.current_index:
                print(f">> {i + 1}. {option}")
            else:
                print(f"   {i + 1}. {option}")
        
    def handle_input(self, key: str):
        """Gère l'entrée utilisateur"""
        if key == 'up':
            self.current_index = max(0, self.current_index - 1)
        elif key == 'down':
            self.current_index = min(len(self.current_menu) - 1, self.current_index + 1)
        elif key == 'enter':
            self.select_option()
        elif key == 'back':
            self.go_back()
        
        self.show_menu()
        
    def select_option(self):
        """Sélectionne l'option actuelle"""
        selected = self.current_menu[self.current_index]
        
        # Gérer les sous-menus
        if selected in menus:
            self.menu_stack.append(selected)
            self.current_menu = menus[selected]
            self.current_index = 0
            return
            
        # Gérer les payloads
        if selected in ['Windows', 'Linux', 'MacOS']:
            self.menu_stack.append(f"{selected.lower()}_payloads")
            self.current_menu = menus[f"{selected.lower()}_payloads"]
            self.current_index = 0
            return
            
        # Gérer l'exécution des payloads
        if selected.endswith('.py') or selected.endswith('.json'):
            payload_id = selected[:-3] if selected.endswith('.py') else selected[:-5]
            self.execute_payload(payload_id)
            return
            
        print(f"Option sélectionnée: {selected}")
        time.sleep(1)
        
    def go_back(self):
        """Retourne au menu précédent"""
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
            self.current_menu = menus[self.menu_stack[-1]]
            self.current_index = 0
            
    def execute_payload(self, payload_id: str):
        """Exécute un payload"""
        print(f"\n=== Exécution du payload: {payload_id} ===")
        
        # Exécuter le payload avec les composants mock
        if not self.payload_manager.execute_payload(
            payload_id,
            keyboard=self.hardware['keyboard'],
            mouse=self.hardware['mouse'],
            consumer_control=self.hardware['consumer_control']
        ):
            print("\nErreur lors de l'exécution du payload")
        
        input("\nAppuyez sur Entrée pour continuer...")
        
    def run(self):
        """Démarre le test interactif"""
        print("=== Test interactif Passpartout ===")
        print("Commandes:")
        print("↑/↓ : Navigation dans le menu")
        print("Enter : Sélectionner une option")
        print("B : Retourner au menu précédent")
        print("Q : Quitter")
        print("\nAppuyez sur une touche pour commencer...")
        
        while True:
            self.show_menu()
            
            # Simuler l'entrée utilisateur
            key = input("\nChoisissez une option (↑/↓/Enter/B/Q): ").lower()
            
            if key == 'q':
                print("\nAu revoir!")
                break
                
            self.handle_input(key)

if __name__ == "__main__":
    test = TestInteractif()
    test.run()
