# Passpartout

Clé USB d'accès et de dépannage d'urgence pour systèmes bloqués

## Description

Passpartout est un outil de dépannage et d'accès d'urgence qui transforme votre Raspberry Pi Pico en une clé USB capable de prendre le contrôle de n'importe quel ordinateur Windows/Linux. Conçu pour les situations d'urgence où l'accès normal au système est impossible, Passpartout permet d'exécuter automatiquement des séquences de commandes pour :

- Débloquer des systèmes bloqués
- Accéder aux modes de récupération
- Exécuter des commandes de dépannage
- Contourner des blocages d'accès

Ce projet utilise la bibliothèque Adafruit HID pour communiquer avec votre ordinateur via USB.

## Fonctionnalités

- Simulation de touches clavier
- Simulation de clics de souris
- Contrôle du volume
- Support de plusieurs layouts clavier (US, CRO, UK)
- Gestion des combinaisons de touches
- Support des commandes de défilement
- Détecteur de bouton intégré

## Installation

1. Préparez votre Raspberry Pi Pico
   - Téléchargez CircuitPython depuis https://circuitpython.org/downloads
   - Copiez le fichier .uf2 sur votre Raspberry Pi Pico

2. Configuration du système
   - Mettez votre Raspberry Pi Pico en mode CIRCUITPY
   - Copiez tous les fichiers du projet sur le périphérique CIRCUITPY
   - Assurez-vous que les bibliothèques Adafruit HID sont installées

3. Configuration des bibliothèques
   - Téléchargez la bibliothèque Adafruit HID depuis la CircuitPython Library Bundle
   - Copiez les fichiers nécessaires dans le dossier lib/
   - Les fichiers requis sont :
     - adafruit_hid
     - adafruit_keyboard
     - adafruit_keyboard_layout_us

## Utilisation

## Mode d'emploi en situation d'urgence

1. Insérez la clé USB dans le port USB de l'ordinateur bloqué
2. Le système détecte automatiquement la clé et affiche le menu de configuration
3. Utilisez les touches directionnelles pour naviguer dans le menu
4. Sélectionnez les options appropriées pour votre système
5. Confirmez l'exécution des séquences de dépannage

## Menu de configuration

Le menu de configuration permet de :

1. Identifier le système cible

   - Sélectionner le système d'exploitation (Windows/Linux/Mac)
   - Spécifier la version du système
   - Configurer les paramètres régionaux

2. Personnaliser les séquences de dépannage

   - Choisir les commandes à exécuter
   - Définir l'ordre des opérations
   - Ajuster les délais entre les actions

3. Configurer les options d'exécution

   - Activer/désactiver les messages de confirmation
   - Définir les combinaisons de touches spécifiques
   - Configurer les actions de déblocage

4. Sauvegarder les paramètres
   - Enregistrer la configuration pour les futures utilisations
   - Créer des profils de dépannage personnalisés
   - Exporter/importer les configurations

Le menu est accessible via les touches directionnelles et la touche Entrée pour la sélection.

## Fonctionnalités avancées

- Exécution automatique de séquences de dépannage
- Support de multiples scénarios de dépannage
- Gestion des modes de récupération Windows/Linux
- Support des commandes de déblocage spécifiques
- Interface USB HID complètement silencieuse

- DELAY : Pause en secondes
- PRESS : Appuyer sur des touches
- WRITE : Écrire du texte
- HOLD : Maintenir des touches
- RELEASE : Relâcher toutes les touches
- MOVE : Déplacer la souris
- SCROLL : Défiler la page
- CLICK : Cliquer avec la souris
- VOLUME : Contrôler le volume

## Configuration des scénarios de dépannage

- Le fichier `layout.txt` définit le layout clavier à utiliser
- Le fichier `settings.toml` configure les paramètres de dépannage
- Les fichiers d'exemple (`example-1.txt`) montrent des scénarios de dépannage courants
- Les séquences de commandes peuvent être personnalisées selon le système cible

## Structure du projet

- `code.py` : Programme principal
- `boot.py` : Script de démarrage
- `layout.txt` : Configuration du layout clavier
- `lib/` : Bibliothèques nécessaires
- `example-1.txt` : Exemple de configuration

## Dépendances

- Adafruit CircuitPython
- Adafruit HID Library
- Python Standard Library

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Tests et validation

Pour tester le système et ses fonctionnalités :

1. Test simplifié (recommandé avant la mise sur clé)
   - Exécutez le test simplifié
   ```bash
   python3 test_menu.py
   ```
   - Ce test ne nécessite aucune installation
   - Vérifiez la navigation dans le menu
   - Testez les commandes de base
   - Vérifiez les séquences de déblocage

2. Test avancé (optionnel)
   - Exécutez le test avancé
   ```bash
   python3 test_virtual.py
   ```
   - Ce test simule l'environnement CircuitPython complet
   - Vérifiez toutes les fonctionnalités HID
   - Testez l'intégration avec Adafruit HID
   - Vérifiez la gestion des entrées/sorties

2. Test sur clé USB
   - Préparez votre environnement
   - Assurez-vous que votre Raspberry Pi Pico est en mode CIRCUITPY
   - Les fichiers du projet doivent être copiés sur CIRCUITPY
   - Les bibliothèques Adafruit doivent être installées dans le dossier lib/

2. Exécution des tests
   - Branchez votre Raspberry Pi Pico à l'ordinateur
   - Le menu de configuration s'affichera automatiquement
   - Utilisez les touches directionnelles pour naviguer
   - Testez les différentes commandes et séquences

3. Tests spécifiques
   - Vérifiez que le menu s'affiche correctement
   - Testez la navigation entre les différents menus
   - Vérifiez les combinaisons de touches
   - Testez les délais de réponse
   - Vérifiez la détection automatique du système

## Installation des bibliothèques

Pour installer les bibliothèques nécessaires :

1. Exécutez le script d'installation
```bash
python3 install_libs.py
```

2. Les bibliothèques requises seront automatiquement téléchargées et installées
3. Les fichiers seront copiés dans le dossier lib/

Note : Assurez-vous d'avoir Internet pour télécharger le bundle Adafruit.

## Sécurité et responsabilité

Ce projet est destiné uniquement à des fins de dépannage et d'accès d'urgence légitimes. Son utilisation doit se faire dans le respect des politiques de sécurité et des lois applicables. Les développeurs ne sont pas responsables de l'utilisation abusive de cet outil.

## Crédits

Ce projet utilise la bibliothèque HID d'Adafruit et est conçu pour être un outil de dépannage professionnel.
