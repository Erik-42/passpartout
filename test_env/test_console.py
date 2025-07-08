#!/usr/bin/env python
import sys
import os

# Ajouter le répertoire parent au PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.os_detector import OSDetector

def main():
    print("=== Détection du système ===")
    
    # Détecter le système d'exploitation
    os_detector = OSDetector()
    os_info = os_detector.get_os_parameters()
    
    print("\nInformations du système:")
    try:
        print(f"Système: {os_info['os_info']['name']} {os_info['os_info']['version']}")
        print(f"Architecture: {os_info['os_info']['architecture']}")
        print(f"Langue: {os_info['system_info']['locale']}")
        print(f"Distribution: {os_info['os_info'].get('distribution', 'Non spécifiée')}")
        print(f"Utilisateur: {os_info['system_info']['username']}")
        print(f"Hôte: {os_info['system_info']['hostname']}")
    except KeyError as e:
        print(f"Erreur: Impossible d'accéder à l'information {str(e)}")
        print("Certaines informations système ne sont pas disponibles")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAu revoir!")
    except Exception as e:
        print(f"\nUne erreur est survenue : {str(e)}")



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAu revoir!")
    except Exception as e:
        print(f"\nUne erreur est survenue : {str(e)}")
