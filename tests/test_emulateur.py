import keyboard
import time
import sys

class Emulateur:
    def __init__(self):
        self.touches = []
        self.texte = ""
        
    def simuler_commande(self, commande, texte=None):
        print(f"\n=== Simulation de la commande : {commande} ===")
        
        # Décoder la commande
        touches = commande.split(" + ")
        touches = [t.strip() for t in touches]
        
        # Afficher les touches à appuyer
        print(f"Touches à appuyer : {touches}")
        
        # Attendre que l'utilisateur soit prêt
        input("Appuyez sur Entrée quand vous êtes prêt à simuler...")
        
        # Simuler l'appui des touches
        print("\nSimulation en cours...")
        print("(Appuyez sur Ctrl+C pour arrêter la simulation)")
        
        try:
            # Appuyer sur toutes les touches
            for touche in touches:
                print(f"Appuyant sur {touche}")
                keyboard.press(touche)
                time.sleep(0.1)
            
            # Maintenir les touches pendant 2 secondes
            time.sleep(2)
            
            # Relâcher toutes les touches
            for touche in touches:
                print(f"Relâchant {touche}")
                keyboard.release(touche)
                time.sleep(0.1)
            
            if texte:
                print(f"\nÉcriture du texte : {texte}")
                keyboard.write(texte)
                time.sleep(0.5)
                keyboard.press_and_release('enter')
                
            print("\nSimulation terminée !")
            
        except KeyboardInterrupt:
            print("\nSimulation arrêtée par l'utilisateur")
            for touche in touches:
                keyboard.release(touche)

def main():
    print("=== Émulateur de Passpartout ===")
    print("\nCe programme vous permet de tester les commandes du système Passpartout")
    print("sans risque pour votre système d'exploitation.")
    print("\nInstructions :")
    print("1. Positionnez votre curseur sur l'application ou le champ où vous voulez tester")
    print("2. Lisez attentivement les touches à appuyer")
    print("3. Appuyez sur Entrée quand vous êtes prêt à simuler")
    print("4. Appuyez sur Ctrl+C pour arrêter la simulation en cours")
    
    # Créer l'émulateur
    emulateur = Emulateur()
    
    # Menu des commandes à tester
    commandes = {
        "Windows": [
            "Ctrl + Alt + Del",
            "Ctrl + Shift + Esc",
            "Win + R"
        ],
        "Mac": [
            "Command + Option + R",
            "Command + Option + P + R",
            "Command + Shift",
            "Command + Option + Esc"
        ],
        "Linux": [
            "Ctrl + Alt + F1",
            "Ctrl + Alt + F2",
            "Ctrl + Alt + Delete"
        ]
    }
    
    while True:
        print("\n=== Menu des commandes ===")
        print("1. Windows")
        print("2. Mac")
        print("3. Linux")
        print("4. Quitter")
        
        choix = input("\nChoisissez une option (1-4) : ")
        
        if choix == "4":
            print("\nAu revoir !")
            break
            
        if choix not in ["1", "2", "3"]:
            print("Option invalide. Veuillez réessayer.")
            continue
            
        # Sélectionner le système
        systeme = "Windows" if choix == "1" else "Mac" if choix == "2" else "Linux"
        print(f"\n=== Commandes {systeme} ===")
        
        # Afficher les commandes disponibles
        for i, commande in enumerate(commandes[systeme], 1):
            print(f"{i}. {commande}")
        
        # Demander la commande à tester
        choix_commande = input("\nChoisissez une commande à tester (1-3) : ")
        
        if choix_commande not in ["1", "2", "3"]:
            print("Option invalide. Veuillez réessayer.")
            continue
            
        # Simuler la commande
        commande = commandes[systeme][int(choix_commande) - 1]
        emulateur.simuler_commande(commande)

if __name__ == "__main__":
    main()
