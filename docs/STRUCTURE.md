# Structure du projet Passpartout

```
passpartout/
├── docs/                 # Documentation
│   ├── README.md        # Documentation principale
│   └── STRUCTURE.md     # Structure du projet
│
├── src/                 # Code source principal
│   ├── code.py         # Code principal
│   ├── menu.py        # Interface utilisateur
│   └── install_libs.py # Installation des bibliothèques
│
├── tests/              # Fichiers de test
│   ├── test_menu.py    # Test simplifié du menu
│   ├── test_virtual.py # Test virtuel
│   └── test_simplifie.py # Test simplifié
│
├── assets/            # Ressources
│   └── images/        # Images et logos
│
├── lib/              # Bibliothèques Adafruit HID
│   └── adafruit_hid/ # Bibliothèque HID
│
└── requirements.txt  # Dépendances Python
```

## Description des dossiers

### `docs/`
- Documentation du projet
- Guides d'utilisation
- Instructions d'installation

### `src/`
- Code source principal du projet
- Fichiers exécutables
- Scripts d'installation

### `tests/`
- Tests unitaires
- Tests de fonctionnalité
- Tests d'intégration

### `assets/`
- Images et logos
- Documentation technique
- Spécifications

### `lib/`
- Bibliothèques externes
- Modules Adafruit HID
- Autres dépendances

## Organisation des fichiers

### Fichiers principaux
- `code.py` : Code principal du programme
- `menu.py` : Interface utilisateur
- `install_libs.py` : Script d'installation des bibliothèques

### Fichiers de test
- `test_menu.py` : Test simplifié du menu
- `test_virtual.py` : Test virtuel complet
- `test_simplifie.py` : Test simplifié des fonctionnalités
