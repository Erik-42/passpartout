import os
import shutil
import zipfile
import urllib.request

# Configuration
LIBS_URL = "https://circuitpython.org/libraries/7.x/latest/adafruit-circuitpython-bundle-7.x-mpy-20250707.zip"
LIBS_DIR = "lib"
REQUIRED_LIBS = [
    "adafruit_hid",
    "adafruit_keyboard",
    "adafruit_keyboard_layout_us",
]

def download_bundle():
    """Télécharge le bundle Adafruit"""
    print("Téléchargement du bundle Adafruit...")
    urllib.request.urlretrieve(LIBS_URL, "adafruit_bundle.zip")
    print("Téléchargement terminé!")

def extract_bundle():
    """Extrait les bibliothèques nécessaires"""
    print("Extraction des bibliothèques...")
    with zipfile.ZipFile("adafruit_bundle.zip", 'r') as zip_ref:
        # Crée le dossier lib s'il n'existe pas
        if not os.path.exists(LIBS_DIR):
            os.makedirs(LIBS_DIR)
        
        # Extrait les bibliothèques requises
        for lib in REQUIRED_LIBS:
            for file in zip_ref.namelist():
                if file.startswith(f"lib/{lib}"):
                    zip_ref.extract(file, ".")
                    # Copie le fichier dans le dossier lib
                    dest_path = os.path.join(LIBS_DIR, os.path.basename(file))
                    src_path = os.path.join("lib", file)
                    shutil.copy2(src_path, dest_path)
                    print(f"Copié: {file}")

def clean_up():
    """Nettoie les fichiers temporaires"""
    print("Nettoyage...")
    if os.path.exists("adafruit_bundle.zip"):
        os.remove("adafruit_bundle.zip")
    if os.path.exists("lib"):
        shutil.rmtree("lib")

def main():
    try:
        download_bundle()
        extract_bundle()
        print("\nInstallation terminée avec succès!")
        print("Les bibliothèques nécessaires ont été installées dans le dossier lib/")
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")
    finally:
        clean_up()

if __name__ == "__main__":
    main()
