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

1. Installez CircuitPython sur votre Raspberry Pi Pico
2. Copiez tous les fichiers du projet sur votre Raspberry Pi Pico
3. Assurez-vous d'avoir les bibliothèques Adafruit HID installées

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
   - Sélectionner le système d'exploitation (Windows/Linux)
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

## Sécurité et responsabilité

Ce projet est destiné uniquement à des fins de dépannage et d'accès d'urgence légitimes. Son utilisation doit se faire dans le respect des politiques de sécurité et des lois applicables. Les développeurs ne sont pas responsables de l'utilisation abusive de cet outil.

## Crédits

Ce projet utilise la bibliothèque HID d'Adafruit et est conçu pour être un outil de dépannage professionnel.
