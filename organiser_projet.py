import os
import shutil

def organiser_fichiers():
    print("=== Organisation du projet Passpartout ===")
    
    # Dossiers de destination
    dossiers = {
        'src': ['boot.py', 'pico_usb.txt', 'layout.txt', 'example-1.txt'],
        'tests': ['preparer_cle.py'],
        'docs': ['README.md', 'STRUCTURE.md', 'LICENSE'],
        'assets/images': ['*.webp'],
        'lib': ['lib/*']
    }
    
    # Créer les dossiers s'ils n'existent pas
    for dossier in dossiers:
        os.makedirs(dossier, exist_ok=True)
    
    # Déplacer les fichiers
    for dossier, fichiers in dossiers.items():
        for fichier in fichiers:
            try:
                # Supporter les patterns comme '*.webp'
                if '*' in fichier:
                    for f in os.listdir('.'):  # Chercher dans le dossier courant
                        if f.endswith('.webp'):
                            shutil.move(f, os.path.join(dossier, f))
                else:
                    if os.path.exists(fichier):
                        shutil.move(fichier, dossier)
                        print(f"✓ Déplacé : {fichier} -> {dossier}")
                    else:
                        print(f"✗ {fichier} non trouvé")
            except Exception as e:
                print(f"✗ Erreur lors du déplacement de {fichier}: {str(e)}")
    
    # Nettoyer les dossiers vides
    dossiers_a_supprimer = ['alter', '__pycache__', '.venv', 'venv']
    for dossier in dossiers_a_supprimer:
        if os.path.exists(dossier):
            try:
                shutil.rmtree(dossier)
                print(f"✓ Supprimé : {dossier}")
            except:
                print(f"✗ Impossible de supprimer {dossier}")
    
    print("\nOrganisation terminée !")

if __name__ == "__main__":
    organiser_fichiers()
