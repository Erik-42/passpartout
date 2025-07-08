import os
import shutil
import sys

def verifier_espace_disponible(chemin):
    """Vérifie l'espace disponible sur la clé USB"""
    try:
        total, used, free = shutil.disk_usage(chemin)
        print(f"\nEspace disponible sur la clé USB : {free // (1024 * 1024)} Mo")
        return free
    except:
        print("Impossible de vérifier l'espace disponible")
        return 0

def copier_fichiers_necessaires():
    """Copie uniquement les fichiers nécessaires pour CircuitPython"""
    # Chemin de la clé USB
    cle_usb = "/media/erik42/CIRCUITPY"
    
    # Vérifier si la clé est accessible
    if not os.path.exists(cle_usb):
        print(f"\nErreur : Le chemin {cle_usb} n'est pas accessible")
        sys.exit(1)
    
    # Vérifier l'espace disponible
    espace_disponible = verifier_espace_disponible(cle_usb)
    if espace_disponible < 1024 * 1024 * 1:  # 1Mo minimum
        print("\nErreur : Espace insuffisant sur la clé USB")
        sys.exit(1)
    
    print("\nDébut de la copie des fichiers nécessaires...")
    
    # Copier les fichiers principaux
    fichiers_principaux = [
        "code.py",
        "menu.py"
    ]
    
    for fichier in fichiers_principaux:
        if os.path.exists(fichier):
            try:
                shutil.copy(fichier, cle_usb)
                print(f"✓ Copié : {fichier} -> {cle_usb}")
            except Exception as e:
                print(f"✗ Erreur lors de la copie de {fichier}: {str(e)}")
        else:
            print(f"✗ {fichier} non trouvé")
    
    # Copier les bibliothèques nécessaires
    if os.path.exists("lib"):
        # Copier uniquement les fichiers nécessaires de adafruit_hid
        if os.path.exists("lib/adafruit_hid"):
            try:
                # Créer le dossier lib s'il n'existe pas
                os.makedirs(os.path.join(cle_usb, "lib"), exist_ok=True)
                
                # Copier uniquement les fichiers nécessaires
                for fichier in os.listdir("lib/adafruit_hid"):
                    if fichier.endswith(".py"):
                        src = os.path.join("lib/adafruit_hid", fichier)
                        dst = os.path.join(cle_usb, "lib", "adafruit_hid", fichier)
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy(src, dst)
                        print(f"✓ Copié : {src} -> {dst}")
            except Exception as e:
                print(f"✗ Erreur lors de la copie des bibliothèques: {str(e)}")
        else:
            print("✗ Le dossier lib/adafruit_hid n'est pas présent")
    else:
        print("✗ Le dossier lib n'est pas présent")
        print("Assurez-vous d'avoir installé les bibliothèques Adafruit HID")
    
    print("\nCopie terminée !")
    print("Vérifiez que tous les fichiers nécessaires sont présents sur la clé USB")

def main():
    print("=== Préparation de la clé USB pour CircuitPython ===")
    print("\nCe script copiera uniquement les fichiers nécessaires sur votre clé USB")
    print("Assurez-vous que votre clé USB CIRCUITPY est bien connectée")
    
    # Attendre que l'utilisateur soit prêt
    input("\nAppuyez sur Entrée quand vous êtes prêt à continuer...")
    
    # Copier les fichiers
    copier_fichiers_necessaires()

if __name__ == "__main__":
    main()
