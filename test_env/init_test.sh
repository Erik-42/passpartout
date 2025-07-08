#!/bin/bash

# Créer les dossiers nécessaires
mkdir -p src payloads

# Créer les fichiers sources
mkdir -p src src/payloads

cat > src/menu.py << 'EOF'
# Menu simplifié pour le test
menus = {
    'main': [
        "Système d'exploitation",
        "Séquences de dépannage",
        "Payloads",
        "Options d'exécution",
        "Sauvegarder",
        "Exécuter"
    ],
    'os': [
        "Windows",
        "Linux",
        "MacOS",
        "Version...",
        "Paramètres régionaux..."
    ]
}
EOF

cat > src/code.py << 'EOF'
# Code simplifié pour le test
def execute_payload(payload_id, keyboard, mouse, consumer_control):
    print(f"Exécution du payload {payload_id}")
    return True
EOF

cat > src/payloads/__init__.py << 'EOF'
class PayloadManager:
    def __init__(self):
        pass
    
    def get_payloads(self):
        return []
EOF

# Copier les fichiers de test
cp test_console.py .

# Créer les payloads de test
mkdir -p payloads
if [ ! -f payloads/test_payloads.json ]; then
cat > payloads/test_payloads.json << 'EOF'
[
    {
        "id": "win_recovery",
        "name": "Windows Recovery Mode",
        "description": "Enters Windows Recovery Mode",
        "os": "Windows",
        "os_version": "10",
        "architecture": "x64",
        "actions": [
            {"type": "press", "keys": ["windows", "r"]},
            {"type": "write", "text": "shutdown /r /o /t 0"},
            {"type": "press", "keys": ["enter"]}
        ]
    },
    {
        "id": "linux_update",
        "name": "Linux System Update",
        "description": "Updates Linux system packages",
        "os": "Linux",
        "os_distribution": "Ubuntu",
        "actions": [
            {"type": "press", "keys": ["ctrl", "alt", "t"]},
            {"type": "write", "text": "sudo apt update && sudo apt upgrade -y"},
            {"type": "press", "keys": ["enter"]}
        ]
    },
    {
        "id": "macos_reboot",
        "name": "MacOS Reboot",
        "description": "Reboots MacOS system",
        "os": "MacOS",
        "os_version": "13.0",
        "actions": [
            {"type": "press", "keys": ["command", "control", "alt", "power"]}
        ]
    }
]
EOF
fi

# Créer le dossier pour les fichiers de test
cp ../tests/test_console.py .

# Rendre les scripts exécutables
chmod +x test_console.py
chmod +x init_test.sh

# Installer les dépendances
pip install -r ../requirements.txt 2>/dev/null || true

echo "\nEnvironnement de test initialisé avec succès !"
