#!/bin/bash

echo "=== Démarrage des tests interactifs Passpartout ==="

cd ..  # Retourner au dossier parent

# Créer un environnement virtuel
python3 -m venv test_env
source test_env/bin/activate

# Installer les dépendances
pip install adafruit-circuitpython-hid

# Copier les fichiers nécessaires pour le test
mkdir -p test_env/{src,payloads,tests}
rsync -av src/payloads/ test_env/payloads/
cp src/menu.py test_env/src/
cp src/code.py test_env/src/
cp tests/test_interactif.py test_env/
cp tests/mock_hardware.py test_env/
cp tests/mock_storage.py test_env/

# Lancer le test interactif
cd test_env
python test_interactif.py

# Nettoyer après utilisation
cd ..
deactivate
rm -rf test_env

exit 0
