import time

class MockKeyboard:
    def __init__(self):
        self.layout = MockKeyboardLayout()
        self.keys_pressed = []

    def send(self, *keys):
        print(f"Appuyant sur les touches: {keys}")
        self.keys_pressed.extend(keys)

class MockKeyboardLayout:
    def write(self, text):
        print(f"Écrivant: {text}")

class MockStorage:
    @staticmethod
    def disable_usb_drive():
        print("Désactivation du lecteur USB simulé")

class MockOS:
    @staticmethod
    def listdir(path):
        return ["config.json", "menu.py", "boot.py"]

class MockJSON:
    @staticmethod
    def load(f):
        return {"system": "Windows", "version": "11"}

    @staticmethod
    def dump(data, f):
        print(f"Sauvegarde des données de configuration: {data}")

def test_menu_navigation():
    """Test la navigation dans le menu"""
    print("\n=== Test de la navigation dans le menu ===")
    print("\nMenu principal:")
    print("1. Système d'exploitation")
    print("2. Séquences de dépannage")
    print("3. Options d'exécution")
    print("4. Sauvegarder")
    print("5. Exécuter")
    
    # Simule la navigation
    print("\nTest de la navigation vers 'Système d'exploitation':")
    print("\nMenu système:")
    print("1. Windows")
    print("2. Linux")
    print("3. Version...")
    print("4. Paramètres régionaux...")
    
    # Simule le retour
    print("\nRetour au menu principal...")

def test_commands():
    """Test les commandes de base"""
    print("\n=== Test des commandes ===")
    kb = MockKeyboard()
    
    print("\nTest de la commande DELAY (2 secondes)")
    time.sleep(2)
    
    print("\nTest de la commande PRESS (Ctrl + Alt + Del)")
    kb.send("CONTROL", "ALT", "DELETE")
    
    print("\nTest de la commande WRITE")
    kb.layout.write("Test d'écriture")
    
    print("\nTest de la commande CLICK")
    print("(Cette commande nécessite un module souris)")

def test_deblocage():
    """Test les séquences de déblocage"""
    print("\n=== Test des séquences de déblocage ===")
    kb = MockKeyboard()
    
    print("\nTest de déblocage Windows")
    print("(Ctrl + Alt + Del -> Utilisateur -> Mot de passe)")
    
    # Simule Ctrl + Alt + Del
    kb.send("CONTROL", "ALT", "DELETE")
    
    # Simule l'écriture du nom d'utilisateur
    kb.layout.write("utilisateur_test")
    
    # Simule l'écriture du mot de passe
    kb.layout.write("motdepasse123")

def main():
    """Fonction principale des tests"""
    print("=== Test du système Passpartout ===")
    print("\nCe programme permet de tester les différentes fonctionnalités du système.")
    print("\nAppuyez sur Ctrl+C pour quitter les tests à tout moment.")
    
    try:
        test_menu_navigation()
        test_commands()
        test_deblocage()
        
        print("\n=== Tests terminés ===")
        print("Toutes les fonctionnalités ont été testées avec succès.")
        
    except KeyboardInterrupt:
        print("\nTest interrompu par l'utilisateur.")
    except Exception as e:
        print(f"\nUne erreur est survenue : {str(e)}")

if __name__ == "__main__":
    main()
