#!/usr/bin/env python3
import sys
import os
import json

# Ajouter le répertoire parent au PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Définir les mocks
class MockBoard:
    GP28 = "GP28"
    GP25 = "GP25"

class MockDirection:
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"

class MockPull:
    UP = "UP"

class MockNeoPixel:
    def __init__(self, pin, count):
        self.pin = pin
        self.count = count
        self.color = (0, 0, 0)
    
    def __setitem__(self, index, color):
        self.color = color
        print(f"LED {index}: {color}")

class MockDigitalInOut:
    class DigitalInOut:
        def __init__(self, pin):
            self.value = True
            self.pin = pin
            print(f"Initialisation du pin {pin}")
        
        def __setattr__(self, name, value):
            if name == 'value':
                print(f"Pin {self.pin}: {'ON' if value else 'OFF'}")
            super().__setattr__(name, value)

# Simuler les modules
sys.modules['board'] = MockBoard
sys.modules['digitalio'] = MockDigitalInOut
sys.modules['digitalio.DigitalInOut'] = MockDigitalInOut.DigitalInOut
sys.modules['digitalio.Direction'] = MockDirection
sys.modules['digitalio.Pull'] = MockPull
sys.modules['neopixel'] = MockNeoPixel

# Simuler le module supervisor
from src.mock_supervisor import MockSupervisor
sys.modules['supervisor'] = MockSupervisor

sys.modules['digitalio'] = MockDigitalInOut
sys.modules['digitalio.Direction'] = MockDirection
sys.modules['digitalio.Pull'] = MockPull
sys.modules['neopixel'] = MockNeoPixel

# Charger le code principal
from src.main import main

# Simuler l'exécution
async def test():
    print("=== Test du système Passpartout ===")
    print("\nConfiguration initiale:")
    
    # Sauvegarder une configuration de test
    test_config = {
        'selected_os': 'windows',
        'selected_payload': 'recovery',
        'auto_execute': True
    }
    
    with open('payloads/config.json', 'w') as f:
        json.dump(test_config, f)
    
    print("\nExécution du code principal...")
    await main()

if __name__ == "__main__":
    import asyncio
    asyncio.run(test())
