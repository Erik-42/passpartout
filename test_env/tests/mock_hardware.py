import time
import random
from typing import List, Any

class MockKeyboard:
    """Simule un clavier HID"""
    def __init__(self):
        self._pressed_keys = set()
        self._layout = MockKeyboardLayout()
        
    def send(self, *keys: List[Any]):
        """Simule l'envoi de touches"""
        print(f"Appui sur touches: {keys}")
        self._pressed_keys.update(keys)
        time.sleep(0.1)  # Simule la latence
        
    def release_all(self):
        """Simule la libération de toutes les touches"""
        print("Libération de toutes les touches")
        self._pressed_keys.clear()
        
    def write(self, text: str):
        """Simule l'écriture de texte"""
        print(f"Écriture: {text}")
        time.sleep(0.1 * len(text))  # Simule la latence

class MockKeyboardLayout:
    """Simule le layout du clavier"""
    def __init__(self):
        self._layout = "US"
        
    def write(self, text: str):
        """Simule l'écriture de texte avec le layout"""
        print(f"Écriture avec layout {self._layout}: {text}")

class MockMouse:
    """Simule une souris HID"""
    def __init__(self):
        self._position = (0, 0)
        
    def click(self, button: int):
        """Simule un clic de souris"""
        print(f"Clic sur bouton {button} à {self._position}")
        time.sleep(0.1)  # Simule la latence
        
    def move(self, x: int, y: int):
        """Simule le déplacement de la souris"""
        self._position = (self._position[0] + x, self._position[1] + y)
        print(f"Déplacement de la souris à {self._position}")
        time.sleep(0.1)  # Simule la latence

class MockConsumerControl:
    """Simule le contrôle du volume et des médias"""
    def send(self, code: int):
        """Simule l'envoi d'un code de consommateur"""
        codes = {
            96: "Volume down",
            97: "Volume mute",
            102: "Volume up"
        }
        print(f"Contrôle: {codes.get(code, 'Code inconnu')}")
        time.sleep(0.1)  # Simule la latence

class MockStorage:
    """Simule le stockage USB"""
    def __init__(self):
        self._enabled = True
        
    def disable_usb_drive(self):
        """Simule la désactivation du lecteur USB"""
        self._enabled = False
        print("Lecteur USB désactivé")
        
    def enable_usb_drive(self):
        """Simule la réactivation du lecteur USB"""
        self._enabled = True
        print("Lecteur USB réactivé")

class MockGPIO:
    """Simule les pins GPIO"""
    def __init__(self):
        self._pins = {}
        
    def setup(self, pin: int, mode: str):
        """Simule la configuration d'une pin"""
        self._pins[pin] = {'mode': mode, 'value': 0}
        
    def input(self, pin: int) -> int:
        """Simule la lecture d'une pin"""
        return self._pins[pin]['value']
        
    def output(self, pin: int, value: int):
        """Simule l'écriture sur une pin"""
        self._pins[pin]['value'] = value

def create_hardware():
    """Crée toutes les instances mock nécessaires"""
    return {
        'keyboard': MockKeyboard(),
        'mouse': MockMouse(),
        'consumer_control': MockConsumerControl(),
        'storage': MockStorage(),
        'gpio': MockGPIO()
    }
