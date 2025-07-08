import board
import digitalio
import time
import json
import supervisor

# Configuration des GPIO
GPIO_BUTTON = board.GP28  # Bouton pour le menu
GPIO_LED = board.GP25     # LED pour les indicateurs

# Initialisation des composants
button = digitalio.DigitalInOut(GPIO_BUTTON)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(GPIO_LED)
led.direction = digitalio.Direction.OUTPUT

# Charger la configuration
def load_config():
    try:
        with open('payloads/config.json', 'r') as f:
            return json.load(f)
    except:
        return {
            'selected_os': None,
            'selected_payload': None,
            'auto_execute': False
        }

# Exécuter un payload
async def execute_payload(os_name, payload_name):
    from payloads import config
    
    # Charger les payloads par défaut
    payloads = config.DEFAULT_PAYLOADS.get(os_name.lower())
    if not payloads:
        print(f"Système {os_name} non supporté")
        return False
    
    payload = payloads.get(payload_name.lower())
    if not payload:
        print(f"Payload {payload_name} non trouvé")
        return False
    
    # Exécuter les actions du payload
    for action in payload['actions']:
        if action['type'] == 'key':
            # Simuler les touches du clavier
            print(f"Appuyant sur les touches: {action['keys']}")
            # TODO: Implémenter l'envoi des touches
            
        elif action['type'] == 'write':
            # Simuler l'écriture
            print(f"Écriture: {action['text']}")
            # TODO: Implémenter l'écriture
            
        await asyncio.sleep(0.1)  # Petite pause entre les actions
    
    return True

async def main():
    # Charger la configuration
    config = load_config()
    
    # Vérifier si l'auto-exécution est activée
    if config['auto_execute'] and config['selected_os'] and config['selected_payload']:
        print("Auto-exécution activée, exécution du payload...")
        led.value = True  # Allumer la LED pendant l'exécution
        await execute_payload(config['selected_os'], config['selected_payload'])
        led.value = False  # Éteindre la LED
        
        # Redémarrer le programme
        supervisor.reload()
    
    # Attendre le bouton pour le menu
    while button.value:  # Bouton non pressé
        await asyncio.sleep(0.1)
    
    # Lancer le menu
    from menu import run_menu
    await run_menu()

# Point d'entrée du programme
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
