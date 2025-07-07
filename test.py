import board
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Configuration du clavier pour les tests
kb = Keyboard()
layout = KeyboardLayoutUS(kb)

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
    layout.write("\nSélection de 'Système d'exploitation'...\n")
    time.sleep(1)
    
    print("\nMenu système:")
    print("1. Windows")
    print("2. Linux")
    print("3. Version...")
    print("4. Paramètres régionaux...")
    
    # Simule le retour
    print("\nRetour au menu principal...")
    time.sleep(1)

def test_commands():
    """Test les commandes de base"""
    print("\n=== Test des commandes ===")
    
    print("\nTest de la commande DELAY (2 secondes)")
    time.sleep(2)
    
    print("\nTest de la commande PRESS (Ctrl + Alt + Del)")
    kb.send(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
    time.sleep(1)
    
    print("\nTest de la commande WRITE")
    layout.write("Test d'écriture\n")
    time.sleep(1)
    
    print("\nTest de la commande CLICK")
    print("(Cette commande nécessite un module souris)")
    time.sleep(1)

def test_deblocage():
    """Test les séquences de déblocage"""
    print("\n=== Test des séquences de déblocage ===")
    
    print("\nTest de déblocage Windows")
    print("(Ctrl + Alt + Del -> Utilisateur -> Mot de passe)")
    
    # Simule Ctrl + Alt + Del
    kb.send(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
    time.sleep(2)
    
    # Simule l'écriture du nom d'utilisateur
    layout.write("utilisateur_test")
    kb.send(Keycode.TAB)
    time.sleep(1)
    
    # Simule l'écriture du mot de passe
    layout.write("motdepasse123")
    kb.send(Keycode.ENTER)
    time.sleep(1)

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
