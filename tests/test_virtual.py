import sys
import os
import json
from typing import Dict, Any

class MockBoard:
    """Classe qui simule les pins du board CircuitPython"""
    GP15 = "GP15"
    GP14 = "GP14"
    GP13 = "GP13"
    GP12 = "GP12"

class MockDigitalInOut:
    """Classe qui simule les entrées/sorties digitales"""
    def __init__(self, pin):
        self.pin = pin
        self.value = True
        self.direction = None
        self.pull = None

class MockDirection:
    """Classe qui simule les directions des pins"""
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"

class MockPull:
    """Classe qui simule les résistances de pull-up/down"""
    UP = "UP"
    DOWN = "DOWN"

class MockKeyboard:
    """Classe qui simule le clavier HID"""
    def __init__(self):
        self.layout = MockKeyboardLayoutUS()
        self.keys_pressed = []

    def send(self, *keys):
        print(f"Simulant l'envoi des touches: {keys}")
        self.keys_pressed.extend(keys)

class MockKeyboardLayoutUS:
    """Classe qui simule le layout clavier US"""
    def __init__(self):
        self.text = ""

    def write(self, text):
        print(f"Simulant l'écriture du texte: {text}")
        self.text += text

class MockStorage:
    """Classe qui simule le système de stockage"""
    @staticmethod
    def disable_usb_drive():
        print("Désactivation du lecteur USB simulé")

class MockOS:
    """Classe qui simule les opérations système"""
    @staticmethod
    def listdir(path):
        return ["config.json", "menu.py", "boot.py"]

class MockJSON:
    """Classe qui simule les opérations JSON"""
    @staticmethod
    def load(f):
        return {"system": "Windows", "version": "11"}

    @staticmethod
    def dump(data, f):
        print(f"Sauvegarde des données de configuration: {data}")

def mock_board():
    """Configure les mocks pour simuler CircuitPython"""
    sys.modules['board'] = MockBoard
    sys.modules['digitalio'] = MockDigitalInOut
    sys.modules['digitalio.Direction'] = MockDirection
    sys.modules['digitalio.Pull'] = MockPull
    sys.modules['storage'] = MockStorage
    sys.modules['os'] = MockOS
    sys.modules['json'] = MockJSON

def mock_hid():
    """Configure les mocks pour simuler HID"""
    # Création d'un module mock pour adafruit_hid
    mock_hid_module = type('module', (object,), {
        'ConsumerControl': type('ConsumerControl', (object,), {
            'send': lambda self, code: print(f"Simulant l'envoi du code de contrôle: {code}")
        }),
        'Keyboard': type('Keyboard', (object,), {
            'layout': MockKeyboardLayoutUS(),
            'send': lambda self, *keys: print(f"Simulant l'envoi des touches: {keys}")
        }),
        'Mouse': type('Mouse', (object,), {
            'click': lambda self, button: print(f"Simulant le clic de la souris: {button}")
        }),
        'Keycode': type('Keycode', (object,), {
            'CONTROL': 'CONTROL',
            'ALT': 'ALT',
            'DELETE': 'DELETE',
            'ENTER': 'ENTER',
            'TAB': 'TAB'
        }),
        'ConsumerControlCode': type('ConsumerControlCode', (object,), {
            'VOLUME_INCREMENT': 'VOLUME_INCREMENT',
            'VOLUME_DECREMENT': 'VOLUME_DECREMENT',
            'MUTE': 'MUTE'
        })
    })()
    
    # Ajout du module mock à sys.modules
    sys.modules['adafruit_hid'] = mock_hid_module

def main():
    """Point d'entrée du test"""
    print("=== Début du test virtuel ===")
    
    # Configuration des mocks
    mock_board()
    mock_hid()
    
    try:
        # Import du menu avec les mocks
        import menu
        print("\n=== Test du menu ===")
        
        # Test de la configuration
        menu.load_config()
        print("\nTest de la sauvegarde de la configuration")
        menu.save_config()
        
        # Test du menu
        print("\nTest de l'affichage du menu")
        menu.display_menu()
        
        # Test des entrées
        print("\nTest des entrées utilisateur")
        menu.handle_input()
        
        print("\n=== Tests terminés ===")
        
    except Exception as e:
        print(f"\nUne erreur est survenue: {str(e)}")

if __name__ == "__main__":
    main()
