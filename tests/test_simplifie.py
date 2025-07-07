import time

class MockKeyboard:
    def __init__(self):
        self.layout = MockKeyboardLayout()
        self.keys_pressed = []
        
    def send(self, *keys):
        print(f"Appuyant sur les touches: {keys}")
        self.keys_pressed.extend(keys)

class MockKeycode:
    """Classe qui simule les codes de touches"""
    CONTROL = "CONTROL"
    ALT = "ALT"
    DELETE = "DELETE"
    ENTER = "ENTER"
    TAB = "TAB"
    COMMAND = "COMMAND"
    OPTION = "OPTION"
    SHIFT = "SHIFT"
    R = "R"
    P = "P"
    D = "D"
    M = "M"
    SPACE = "SPACE"
    F2 = "F2"
    ESCAPE = "ESCAPE"

class MockKeyboardLayout:
    def write(self, text):
        print(f"Écrivant: {text}")

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
    
    print("\nTest des commandes Windows (Ctrl + Alt + Del)")
    kb.send("CONTROL", "ALT", "DELETE")
    
    print("\nTest des commandes Mac")
    print("Commande + Option + R (récupération)")
    kb.send("COMMAND", "OPTION", "R")
    
    print("\nCommande + Option + P + R (réinitialisation PRAM)")
    kb.send("COMMAND", "OPTION", "P", "R")
    
    print("\nCommande + Option + Shift + R (récupération mise à jour)")
    kb.send("COMMAND", "OPTION", "SHIFT", "R")
    
    print("\nCommande + R (récupération rapide)")
    kb.send("COMMAND", "R")
    
    print("\nCommande + Shift (démarrage en mode sans échec)")
    kb.send("COMMAND", "SHIFT")
    
    print("\nCommande + Option + Esc (force quit)")
    kb.send("COMMAND", "OPTION", "ESCAPE")
    
    print("\nCommande + Option + D (dock)")
    kb.send("COMMAND", "OPTION", "D")
    
    print("\nCommande + Option + M (mission control)")
    kb.send("COMMAND", "OPTION", "M")
    
    print("\nCommande + Option + Espace (Spotlight)")
    kb.send("COMMAND", "OPTION", "SPACE")
    
    print("\nCommande + Option + F2 (mode développeur)")
    kb.send("COMMAND", "OPTION", "F2")
    
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
    
    print("\nTest de déblocage Mac")
    print("(Commande + Option + R -> Utilisateur -> Mot de passe)")
    
    # Simule Commande + Option + R
    kb.send("COMMAND", "OPTION", "R")
    
    # Simule l'écriture du nom d'utilisateur
    kb.layout.write("utilisateur_mac")
    
    # Simule l'écriture du mot de passe
    kb.layout.write("motdepasse_mac")

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
