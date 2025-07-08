import board
import digitalio
import time
import neopixel

# Configuration des GPIO
GPIO_BUTTON = board.GP28  # Bouton pour le menu
GPIO_LED = board.GP25     # LED pour les indicateurs

# Initialisation des composants
button = digitalio.DigitalInOut(GPIO_BUTTON)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led = neopixel.NeoPixel(GPIO_LED, 1)

# Menu principal
menus = {
    'main': [
        "Détecter système",
        "Sélectionner payload",
        "Configurer auto-exécution",
        "Tester payload",
        "Sauvegarder configuration",
        "Quitter"
    ],
    'os': [
        "Windows",
        "Linux",
        "MacOS",
        "Retour"
    ],
    'payloads': {
        'windows': [
            "Recovery Mode",
            "Task Manager",
            "Retour"
        ],
        'linux': [
            "Terminal",
            "System Update",
            "Retour"
        ],
        'macos': [
            "Force Quit",
            "Reboot",
            "Retour"
        ]
    }
}

# État du menu
class MenuState:
    def __init__(self):
        self.current_menu = 'main'
        self.selected_os = None
        self.selected_payload = None
        self.auto_execute = False

    def select_os(self, os_name):
        self.selected_os = os_name
        self.current_menu = 'payloads'

    def select_payload(self, payload_name):
        self.selected_payload = payload_name
        print(f"Payload sélectionné: {payload_name}")

    def toggle_auto_execute(self):
        self.auto_execute = not self.auto_execute
        print(f"Auto-exécution {'activée' if self.auto_execute else 'désactivée'}")

    def save_config(self):
        import json
        with open('payloads/config.json', 'w') as f:
            json.dump({
                'selected_os': self.selected_os,
                'selected_payload': self.selected_payload,
                'auto_execute': self.auto_execute
            }, f)
        print("Configuration sauvegardée")

# Fonction pour clignoter la LED
async def blink_led(color, duration=0.1):
    led[0] = color
    await asyncio.sleep(duration)
    led[0] = (0, 0, 0)
    await asyncio.sleep(duration)

# Fonction principale du menu
async def run_menu():
    state = MenuState()
    
    while True:
        # Clignoter la LED en rouge si un payload est sélectionné
        if state.selected_payload:
            await blink_led((255, 0, 0))
        
        # Afficher le menu
        print("\n=== Menu Passpartout ===")
        print(f"Menu: {state.current_menu}")
        
        # Afficher les options
        if state.current_menu == 'main':
            options = menus['main']
        elif state.current_menu == 'os':
            options = menus['os']
        else:
            options = menus['payloads'].get(state.selected_os, [])
        
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        
        # Attendre l'entrée utilisateur
        if not button.value:  # Bouton pressé
            try:
                choice = int(input("\nChoisissez une option (1-{}): ".format(len(options))))
                
                if 1 <= choice <= len(options):
                    selected = options[choice - 1]
                    
                    if state.current_menu == 'main':
                        if selected == "Détecter système":
                            print("Détection du système...")
                            # TODO: Implémenter la détection du système
                            
                        elif selected == "Sélectionner payload":
                            state.current_menu = 'os'
                            
                        elif selected == "Configurer auto-exécution":
                            state.toggle_auto_execute()
                            
                        elif selected == "Tester payload":
                            if state.selected_payload and state.selected_os:
                                print(f"Test du payload: {state.selected_payload}")
                                # TODO: Implémenter le test du payload
                            else:
                                print("Aucun payload sélectionné")
                                
                        elif selected == "Sauvegarder configuration":
                            state.save_config()
                            
                        elif selected == "Quitter":
                            break
                            
                    elif state.current_menu == 'os':
                        if selected == "Retour":
                            state.current_menu = 'main'
                        else:
                            state.select_os(selected.lower())
                            
                    elif state.current_menu == 'payloads':
                        if selected == "Retour":
                            state.current_menu = 'os'
                        else:
                            state.select_payload(selected)
                            
            except ValueError:
                print("Entrée invalide")
                
        await asyncio.sleep(0.1)  # Pour éviter de saturer le processeur
